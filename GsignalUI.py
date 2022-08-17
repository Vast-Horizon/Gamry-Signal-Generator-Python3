# Form implementation generated from reading ui file 'projectui.ui'
# Created by: PyQt6 UI code generator 6.3.1
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
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
import csv

active = False
        
class GamryCOMError(Exception):
    pass

def gamry_error_decoder(e):
    if isinstance(e, comtypes.COMError):
        hresult = 2**32+e.args[0]
        if hresult & 0x20000000:
            return GamryCOMError('0x{0:08x}: {1}'.format(2**32+e.args[0], e.args[1]))
    return e

class GamryDtaqEvents(object):
    def __init__(self, dtaq):
        self.dtaq = dtaq
        self.acquired_points = []
        
    def cook(self):
        count = 1
        while count > 0:
            count, points = self.dtaq.Cook(32768)
            self.acquired_points.extend(zip(*points))

    def _IGamryDtaqEvents_OnDataAvailable(self, this):
        self.cook()

    def _IGamryDtaqEvents_OnDataDone(self, this):
        self.cook() # a final cook
        time.sleep(2)
        global active
        active = False
        print("DONE")
    


#UI Design
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1356, 776)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.95)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(250, 255, 250)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DataFileButton_1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.openF())
        self.DataFileButton_1.setGeometry(QtCore.QRect(40, 440, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DataFileButton_1.setFont(font)
        self.DataFileButton_1.setStatusTip("")
        self.DataFileButton_1.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.DataFileButton_1.setAutoDefault(False)
        self.DataFileButton_1.setDefault(False)
        self.DataFileButton_1.setFlat(False)
        self.DataFileButton_1.setObjectName("DataFileButton_1")
        self.DataFileButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.loadDefault())
        self.DataFileButton_2.setGeometry(QtCore.QRect(260, 440, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DataFileButton_2.setFont(font)
        self.DataFileButton_2.setStatusTip("")
        self.DataFileButton_2.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.DataFileButton_2.setAutoDefault(False)
        self.DataFileButton_2.setDefault(False)
        self.DataFileButton_2.setFlat(False)
        self.DataFileButton_2.setObjectName("DataFileButton_2")
        self.objNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.objNameEdit.setEnabled(True)
        self.objNameEdit.setGeometry(QtCore.QRect(40, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.objNameEdit.setFont(font)
        self.objNameEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.objNameEdit.setObjectName("objNameEdit")
        self.objNamelabel = QtWidgets.QLabel(self.centralwidget)
        self.objNamelabel.setGeometry(QtCore.QRect(40, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.objNamelabel.setFont(font)
        self.objNamelabel.setObjectName("objNamelabel")
        self.signalPathlabel = QtWidgets.QLabel(self.centralwidget)
        self.signalPathlabel.setGeometry(QtCore.QRect(40, 500, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.signalPathlabel.setFont(font)
        self.signalPathlabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.signalPathlabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.signalPathlabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.signalPathlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signalPathlabel.setObjectName("signalPathlabel")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(530, 30, 781, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda:self.draw())
        self.pushButton.setGeometry(QtCore.QRect(40, 660, 201, 31))
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.ClearPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearPushButton.clicked.connect(lambda:self.clear())
        self.ClearPushButton.setGeometry(QtCore.QRect(270, 660, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.ClearPushButton.setFont(font)
        self.ClearPushButton.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.ClearPushButton.setObjectName("ClearPushButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 30, 391, 141))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("CMHT-Logo.webp"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.IDEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IDEdit.setEnabled(True)
        self.IDEdit.setGeometry(QtCore.QRect(170, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(True)
        self.IDEdit.setFont(font)
        self.IDEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.IDEdit.setObjectName("IDEdit")
        self.IDlabel = QtWidgets.QLabel(self.centralwidget)
        self.IDlabel.setGeometry(QtCore.QRect(170, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.IDlabel.setFont(font)
        self.IDlabel.setObjectName("IDlabel")
        self.TestButton = QtWidgets.QPushButton(self.centralwidget)
        self.TestButton.setGeometry(QtCore.QRect(40, 550, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.TestButton.setFont(font)
        self.TestButton.setStyleSheet("QPushButton{background-color:rgb(220, 255, 210); border:none;\n"
"padding-top:2px; color:rgb(0,0,0); border-radius: 10px; }\n"
"QPushButton:hover{background-color:rgb(191, 255, 128);}\n"
"QPushButton:pressed{background-color:rgb(115, 230, 0);}")
        self.TestButton.setObjectName("TestButton")
        self.TestButton.clicked.connect(lambda:self.initIndicator())
        self.IndicatorLabel = QtWidgets.QLabel(self.centralwidget)
        self.IndicatorLabel.setGeometry(QtCore.QRect(40, 620, 431, 21))
        self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(50,200,50);border: 1.5px solid gray;border-radius: 10px;}")
        self.IndicatorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.IndicatorLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.IndicatorLabel.setObjectName("IndicatorLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QDateEdit {border: 1px solid gray;border-radius: 8px;}")
        self.dateEdit.setGeometry(QtCore.QRect(339, 320, 131, 31))
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        #self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(currentYear, currentMonth, currentDay), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.FrequencyInput = QtWidgets.QLineEdit(self.centralwidget)
        self.FrequencyInput.setGeometry(QtCore.QRect(40, 320, 111, 31))
        self.FrequencyInput.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.FrequencyInput.setObjectName("FrequencyInput")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(170, 320, 61, 31))
        self.spinBox.setStyleSheet("QSpinBox {border: 1px solid gray;border-radius: 8px;}")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.Fqlabel = QtWidgets.QLabel(self.centralwidget)
        self.Fqlabel.setGeometry(QtCore.QRect(40, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fqlabel.setFont(font)
        self.Fqlabel.setObjectName("Fqlabel")
        self.RpeatsLabel = QtWidgets.QLabel(self.centralwidget)
        self.RpeatsLabel.setGeometry(QtCore.QRect(170, 290, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.RpeatsLabel.setFont(font)
        self.RpeatsLabel.setObjectName("RpeatsLabel")
        self.TempEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TempEdit.setEnabled(True)
        self.TempEdit.setGeometry(QtCore.QRect(340, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(True)
        self.TempEdit.setFont(font)
        self.TempEdit.setAutoFillBackground(False)
        self.TempEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.TempEdit.setObjectName("TempEdit")
        self.TestNumEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TestNumEdit.setEnabled(True)
        self.TestNumEdit.setGeometry(QtCore.QRect(260, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(True)
        self.TestNumEdit.setFont(font)
        self.TestNumEdit.setAutoFillBackground(False)
        self.TestNumEdit.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.TestNumEdit.setObjectName("TestNumEdit")
        self.TestNumlabel = QtWidgets.QLabel(self.centralwidget)
        self.TestNumlabel.setGeometry(QtCore.QRect(260, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.TestNumlabel.setFont(font)
        self.TestNumlabel.setObjectName("TestNumlabel")
        self.Temperature = QtWidgets.QLabel(self.centralwidget)
        self.Temperature.setGeometry(QtCore.QRect(340, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.Temperature.setFont(font)
        self.Temperature.setObjectName("Temperature")
        self.DateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DateLabel.setGeometry(QtCore.QRect(340, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(530, 260, 781, 211))
        self.graphicsView_2.setBackground('w')
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(530, 500, 781, 221))
        self.graphicsView_3.setBackground('w')
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.MeasuredVLabel = QtWidgets.QLabel(self.centralwidget)
        self.MeasuredVLabel.setGeometry(QtCore.QRect(830, 480, 241, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MeasuredVLabel.setFont(font)
        self.MeasuredVLabel.setStyleSheet("QLabel{font-weight: bold}")
        self.MeasuredVLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MeasuredVLabel.setObjectName("MeasuredVLabel")
        self.MeasuredcurLabel = QtWidgets.QLabel(self.centralwidget)
        self.MeasuredcurLabel.setGeometry(QtCore.QRect(810, 240, 251, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MeasuredcurLabel.setFont(font)
        self.MeasuredcurLabel.setStyleSheet("QLabel{font-weight: bold}")
        self.MeasuredcurLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MeasuredcurLabel.setObjectName("MeasuredcurLabel")
        self.OutSigLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutSigLabel.setGeometry(QtCore.QRect(840, 10, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OutSigLabel.setFont(font)
        self.OutSigLabel.setAutoFillBackground(False)
        self.OutSigLabel.setStyleSheet("QLabel{font-weight: bold}")
        self.OutSigLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.OutSigLabel.setObjectName("OutSigLabel")
        self.ampInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ampInput.setGeometry(QtCore.QRect(260, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ampInput.setFont(font)
        self.ampInput.setStyleSheet("QLineEdit {border: 1px solid gray;border-radius: 10px;}")
        self.ampInput.setObjectName("ampInput")
        self.ampLabel = QtWidgets.QLabel(self.centralwidget)
        self.ampLabel.setGeometry(QtCore.QRect(260, 290, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.ampLabel.setFont(font)
        self.ampLabel.setObjectName("ampLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1356, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def openF(self):
        global fpath
        fpath = filedialog.askopenfilename()
        self.signalPathlabel.setText(fpath)
       
    def loadDefault(self):
        #self.folderDir()
        global fpath
        fpath = 'InputProfileGalv.csv'
        self.signalPathlabel.setText(fpath)
    
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
            print("Directory already exists")

    def press_it(self,press):
        self.signalPathlabel.setText(press)

    def initIndicator(self):
        self.IndicatorLabel.setText(" ")
        self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(255,224,102);border: 1.5px solid gray;border-radius: 10px;}")   
        self.initialize()
    
    def initialize(self):
        global active
        active=True
        global GamryCOM,pstat,dtaqcpiv,dtaqsink,connection
        GamryCOM=client.GetModule(['{BD962F0D-A990-4823-9CF5-284D1CDD9C6D}', 1, 0])
        devices=client.CreateObject('GamryCOM.GamryDeviceList')
        #Potentiostat object
        pstat=client.CreateObject('GamryCOM.GamryPC6Pstat')
        pstat.Init(devices.EnumSections()[0]) 
        dtaqcpiv=client.CreateObject('GamryCOM.GamryDtaqCpiv')
        dtaqcpiv.Init(pstat)
        #Data acquisition object
        dtaqsink = GamryDtaqEvents(dtaqcpiv)
        connection = client.GetEvents(dtaqcpiv, dtaqsink)
        print("\n========================================================================")
        print(devices.EnumSections()[0], " Initialization Completed")
        self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(255,224,102);border: 1.5px solid gray;border-radius: 10px;}")  
        self.test()
        

    def test(self):
        pstat.Open()
        amp = float(self.ampInput.text())
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
        Sig.Init(pstat, Cycles, SampleRate, numOfPoints, PointsList, GamryCOM.PstatMode)
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

        try:            
            dtaqcpiv.Run(True)
            print("Running\t","Should be ready in 30 second...")
        except Exception as e:
            raise gamry_error_decoder(e)

        while active == True:
            client.PumpEvents(1)
            time.sleep(0.1)

        #Turn off
        while active == False:   
            print("Terminating...")
            print("Total Number of Output Data Points Detected: ", len(dtaqsink.acquired_points))
            pstat.SetCell(GamryCOM.CellOff)
            time.sleep(1)
            pstat.Close()
            #del connection
            gc.collect()
            self.IndicatorLabel.setStyleSheet("QLabel {background-color: rgb(50,200,50);border: 1.5px solid gray;border-radius: 10px;}")
            self.IndicatorLabel.setText(" ")
            try:
                f.close()
                break
            except (NameError, IOError):
                pass
        self.clear()
        self.draw()

        #Save Raw Data
        self.folderDir()
        testnum = self.TestNumEdit.text()
        cellID = self.IDEdit.text()
        subdir = outputPath+"\Test"+testnum +" Cell"+cellID+" data.csv"
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
    
    def clear(self):
        self.graphicsView.clear()
        self.graphicsView_2.clear()
        self.graphicsView_3.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gamry Signal"))
        self.DataFileButton_1.setText(_translate("MainWindow", "Select Signal Profile"))
        self.DataFileButton_2.setText(_translate("MainWindow", "Load Default Profile"))
        self.objNamelabel.setText(_translate("MainWindow", "Model:"))
        self.signalPathlabel.setText(_translate("MainWindow", "Signal Profile"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.ClearPushButton.setText(_translate("MainWindow", "Clear"))
        self.IDlabel.setText(_translate("MainWindow", "Cell ID:"))
        self.TestButton.setText(_translate("MainWindow", "Test"))
        self.IndicatorLabel.setText(_translate("MainWindow", "  "))
        self.FrequencyInput.setText(_translate("MainWindow", "80"))
        self.Fqlabel.setText(_translate("MainWindow", "Freq.[KHz]:"))
        self.RpeatsLabel.setText(_translate("MainWindow", "Cycles:"))
        self.TempEdit.setText(_translate("MainWindow", "23"))
        self.TestNumEdit.setText(_translate("MainWindow", "1"))
        self.TestNumlabel.setText(_translate("MainWindow", "Test #:"))
        self.Temperature.setText(_translate("MainWindow", "Temperature:"))
        self.DateLabel.setText(_translate("MainWindow", "M/d/yyyy:"))
        self.MeasuredVLabel.setText(_translate("MainWindow", "Measured Voltage [V] vs Time [s]"))
        self.MeasuredcurLabel.setText(_translate("MainWindow", "Measured Current [A] vs Time [s]"))
        self.OutSigLabel.setText(_translate("MainWindow", "Output Signal vs Time [s]"))
        self.ampInput.setText(_translate("MainWindow", "1"))
        self.ampLabel.setText(_translate("MainWindow", "Amp. :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
