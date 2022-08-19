from PyQt6 import QtWidgets, uic,QtCore, QtGui
from tkinter import filedialog
from pyqtgraph import PlotWidget

import comtypes
import comtypes.client as client
import gc
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
import sys
import csv
active = False #Flag

############################Gamry Classes#################################
class GamryCOMError(Exception):
    pass

def gamry_error_decoder(e):
    if isinstance(e, comtypes.COMError):
        hresult = 2**32+e.args[0]
        if hresult & 0x20000000:
            return GamryCOMError('0x{0:08x}: {1}'.format(2**32+e.args[0], e.args[1]))
    return e
c = 0
class GamryDtaqEvents(object):
    def __init__(self, dtaq):
        self.dtaq = dtaq
        self.acquired_points = [] #This is a list of tuples with 10 columns of measurement data
        
    def cook(self):
        count = 1
        while count > 0:
            count, points = self.dtaq.Cook(32768)
            self.acquired_points.extend(zip(*points))

    def _IGamryDtaqEvents_OnDataAvailable(self, this):
        self.cook()

    def _IGamryDtaqEvents_OnDataDone(self, this):
        self.cook() # final data acquisition 
        time.sleep(1)
        global active
        active = False
        print("DONE ")

############################################################################
class UI(QtWidgets.QMainWindow):
   #Load UI 
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("projectui.ui", self)
        self.graphicsView.setBackground('w')
        self.graphicsView_2.setBackground('w')
        self.graphicsView_3.setBackground('w')
        #Get current time
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(currentYear, currentMonth, currentDay), QtCore.QTime(0, 0, 0)))
        self.progressBar.setValue(0)
        #Connect buttons with functions
        self.DataFileButton_1.clicked.connect(self.openF)
        self.DataFileButton_2.clicked.connect(self.loadDefault)
        self.pushButton.clicked.connect(self.draw)
        self.ClearPushButton.clicked.connect(self.clear)
        self.TestButton.clicked.connect(self.initialize)
        #Show UI
        self.show()
    #Select Signal Profile
    def openF(self):
        global fpath
        fpath = filedialog.askopenfilename()
        self.signalPathlabel.setText(fpath)

    #Load Default Signal Profile
    def loadDefault(self):
        global fpath
        fpath = 'InputProfileGalv.csv'
        self.signalPathlabel.setText(fpath)
        print(fpath)

    #Creat Directory to save
    def folderDir(self):
        objname = self.objNameEdit.text()
        temperature = self.TempEdit.text()
        testnum = self.TestNumEdit.text()
        dday = str(self.dateEdit.date().day())
        mmonth = str(self.dateEdit.date().month())
        yyyyear = str(self.dateEdit.date().year())
        subdir = "Test"+testnum+"-"+temperature + "degrees-"+mmonth+"-"+dday+"-"+yyyyear
        cdir = os.getcwd() #Get the current directory
        parent_dir = os.path.join(cdir,objname)
        global outputPath
        outputPath = os.path.join(parent_dir,subdir)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        else:
            pass
            #print("Directory already exists")
    
    #UNUSED
    def initIndicator(self):
        self.IndicatorLabel.setText("Please Wait for a while, or check for any error messages ")
        self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(255,224,102);border: 1.5px solid gray;border-radius: 8px;}")   
        #self.initialize()
    
    #Set up connection with the Gamry instrument
    def initialize(self):
        global active
        active=True
        global GamryCOM,pstat,dtaqciiv,dtaqsink,connection
        GamryCOM=client.GetModule(['{BD962F0D-A990-4823-9CF5-284D1CDD9C6D}', 1, 0])
        devices=client.CreateObject('GamryCOM.GamryDeviceList')
        #Gamry Instrument object
        pstat=client.CreateObject('GamryCOM.GamryPC6Pstat')
        pstat.Init(devices.EnumSections()[0]) 
        #Open
        pstat.Open()
        pstat.SetCtrlMode(GamryCOM.GstatMode)#Set it to galvanostat mode
        #Data acquisition object
        dtaqciiv=client.CreateObject('GamryCOM.GamryDtaqCiiv')
        dtaqciiv.Init(pstat)
        dtaqsink = GamryDtaqEvents(dtaqciiv)
        connection = client.GetEvents(dtaqciiv, dtaqsink)
        print("\n========================================================================")
        print(devices.EnumSections()[0], " Initialization Completed")
        self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(255,224,102);border: 1.5px solid gray;border-radius: 8px;}")  
        self.test()

    #To test    
    def test(self):
        #Prepare parameters
        amp = float(self.ampInput.text())
        global numOfPoints
        try:
            f = open(fpath)
            PointsList = f.readlines()
            numOfPoints = len(PointsList)
            PointsList = [float(i)*amp for i in PointsList]
        except (NameError, IOError):
            print("Error - File does not appear to exist.") 
        Cycles = int(self.spinBox.text())
        temprate = float(numOfPoints/(int(self.FrequencyInput.text())*1000)/numOfPoints)
        temprate = round(temprate,8)
        SampleRate = temprate
        Sig=client.CreateObject('GamryCOM.GamrySignalArray')
        Sig.Init(pstat, Cycles, SampleRate, numOfPoints, PointsList, GamryCOM.GstatMode)
        pstat.SetSignal(Sig)

        #Print out information
        print("###################################################")
        print("Number of Data Points of each period: ", numOfPoints)
        print("Number of Cycles: ", Cycles)
        print("Time gap between each output data point in second: ", SampleRate)
        runTime = SampleRate*Cycles*numOfPoints
        print("Estimated total signal length in second: ", runTime)
        print("Frequcency of data point outputing in Hz: ", 1/SampleRate) 
        print("###################################################")
        pstat.SetCell(GamryCOM.CellOn)
        
        #Make it to run
        try:            
            dtaqciiv.Run(True)
            print("Running\t","Should be ready in 30 second...")
        except Exception as e:
            raise gamry_error_decoder(e)
        prograssList = []
        counter = 0
        while active == True:
            client.PumpEvents(1)
            time.sleep(0.1)
            counter+=1
            prograssList.append(counter)
            print(prograssList)
            #self.progressBar.setMinimum(5)
            self.progressBar.setValue(counter)
 

        #Turn off
        while active == False: 
            self.progressBar.setValue(30)  
            print("Terminating...")
            print("Total Number of Output Data Points Detected: ", len(dtaqsink.acquired_points))
            pstat.SetCell(GamryCOM.CellOff)
            time.sleep(1)
            pstat.Close()
            #del connection
            gc.collect()
            self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(50,200,50);border: 1.5px solid gray;border-radius: 8px;}")
            self.IndicatorLabel.setText(" ")
            try:
                f.close()
                break

            except (NameError, IOError):
                pass
        self.progressBar.setValue(0)
        self.clear()
        self.draw()

        #Save Raw Data to the directory
        self.folderDir()
        testnum = self.TestNumEdit.text()
        cellID = self.IDEdit.text()
        model = self.objNameEdit.text()
        subdir = outputPath+"\Test"+testnum +"-Cell"+cellID+model+".csv"
        rawDataList = []
        titleList = ["Time(s)","Measur. V(V)","Uncompens. V","Measur. I(A)","Signal Out","Aux Input","IE Range","Overload Info","Stop","Temp"]
        with open(subdir, 'w') as file_handler:
            for item in dtaqsink.acquired_points:
                rawDataList.append(','.join([str(j) for j in item]))
            writer = csv.writer(file_handler)
            writer.writerow(titleList)
            for item in rawDataList:
                file_handler.write("{}\n".format(item))
        print("Data file ",subdir," is saved")
        print("OFF")
    
    #Process the acquired_points list to plot
    def draw(self):
        timeList = [x[0] for x in dtaqsink.acquired_points]
        voltsList = [x[1] for x in dtaqsink.acquired_points]
        currentList = [x[3] for x in dtaqsink.acquired_points]  
        VsigList = [x[4] for x in dtaqsink.acquired_points]         
        timeList = [float(i) for i in timeList]
        voltsList = [float(j) for j in voltsList]
        currentList = [float(j) for j in currentList]
        VsigList = [float(j) for j in VsigList]
        self.graphicsView.plot(timeList,VsigList,pen=(10,10,200))
        self.graphicsView_2.plot(timeList,currentList,pen=(10,10,200))
        self.graphicsView_3.plot(timeList,voltsList,pen=(10,10,200))
    
    #Clear plots
    def clear(self):
        self.graphicsView.clear()
        self.graphicsView_2.clear()
        self.graphicsView_3.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec())