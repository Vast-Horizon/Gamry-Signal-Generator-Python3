# -*- coding: utf-8 -*-
# Get comtypes from:
# sourceforge -- http://sourceforge.net/projects/comtypes/files/comtypes/
# or
# PyPI -- https://pypi.python.org/pypi/comtypes
from __future__ import print_function
import comtypes
import comtypes.client as client
import gc
import numpy as np
import matplotlib.pyplot as plt
import time

from tkinter import *
from tkinter import filedialog

GamryCOM=client.GetModule(['{BD962F0D-A990-4823-9CF5-284D1CDD9C6D}', 1, 0])

# utilities: #####################
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
            count, points = self.dtaq.Cook(1024)
            self.acquired_points.extend(zip(*points))
        
    def _IGamryDtaqEvents_OnDataAvailable(self, this):
        self.cook()

    def _IGamryDtaqEvents_OnDataDone(self, this):
        self.cook() # a final cook
        time.sleep(2.0)
        stopacq()

def stopacq():

    global active
    global connection
    print("Terminating...")
    active = False
    print("Total Number of Output Data Points Detected: ", len(dtaqsink.acquired_points))
    #Save raw data
    timeOutputList = [x[0] for x in dtaqsink.acquired_points]
    with open('outputTime.txt', 'w') as file_handler:
        for item in timeOutputList:
            file_handler.write("{}\n".format(item))

    voltsOutputList = [x[1] for x in dtaqsink.acquired_points]
    with open('outputVolts.txt', 'w') as file_handler:
        for item in voltsOutputList:
            file_handler.write("{}\n".format(item))
    #Turn off
    pstat.SetCell(GamryCOM.CellOff)
    time.sleep(1)
    pstat.Close()
    del connection
    gc.collect()
    file_handler.close()
    print("OFF")

    #Plot a diagram
    plt.title('Measured Signal')
    plt.xlabel('Time(s)')
    plt.ylabel('Voltage(V)')
    plt.plot(timeOutputList, voltsOutputList)
    plt.show()
    return
###############################

devices=client.CreateObject('GamryCOM.GamryDeviceList')
print(devices.EnumSections())

#Potentiostat object
pstat=client.CreateObject('GamryCOM.GamryPC6Pstat')
pstat.Init(devices.EnumSections()[0]) # grab first pstat

dtaqcpiv=client.CreateObject('GamryCOM.GamryDtaqCpiv')
dtaqcpiv.Init(pstat)

#Data acquisition object
dtaqsink = GamryDtaqEvents(dtaqcpiv)
connection = client.GetEvents(dtaqcpiv, dtaqsink)

#Read the data file
window = Tk(className=' Gamry Potentiostat Signal Generator')
window.geometry("400x100")
window.minsize(400, 100)
window.maxsize(400, 100)
window['background']='#FFFFFF'
def openF():
    global path
    path = filedialog.askopenfilename()
    print(path)
    window.destroy()
    
def loadDefault():
    global path
    path = 'RAMPdata.txt'
    print(path)
    window.destroy()
   
text = Label(window, bg = 'white', fg='#bfe3c4', text="-----------------------------------------------------")
text.place(x=60,y=10)
text = Label(window, bg = 'white', text="The data file should contain a list of voltage points")
text.place(x=60,y=70)
button0 = Button(text="Select Data File", bg = 'white', fg="Blue",width=28, command=openF)
button0.pack(side=LEFT)
button1 = Button(window, text="Load Demo File", bg = 'white', fg="red",width=28,command=loadDefault)
button1.pack(side=RIGHT)
window.mainloop()

#f = open("RAMPdata.txt") #uncomment this to load a demo data file directly
f = open(path)
PointsList = f.readlines()
numOfPoints = len(PointsList)
PointsList = [float(i) for i in PointsList]

#Turn on
pstat.Open()

#Create a signal object then set it to pstat
#SampleRate is the time gap between each point in the list
#Cycles = input("Number of Cycles: ")
#SampleRate = input("Time gap between each output data point in second: ")
Cycles = 3
SampleRate=0.0001
Sig=client.CreateObject('GamryCOM.GamrySignalArray')
Sig.Init(pstat, Cycles, SampleRate, numOfPoints, PointsList, GamryCOM.PstatMode)
pstat.SetSignal(Sig)

#Print out information
print("###################################################")
print("Number of Data Points of each period: ", numOfPoints)
print("Number of Cycles: ", Cycles)
print("Time gap between each output data point in second: ", SampleRate)
runTime = SampleRate*Cycles*numOfPoints
print("Estimated run time in second: ", runTime)
print("Frequcency of data point outputing in Hz: ", 1/SampleRate) 
print("###################################################")
input("READY. Press Enter to start...")
#Start to output signal
pstat.SetCell(GamryCOM.CellOn)
try:
    dtaqcpiv.Run(True)
    print("Running...")
    
except Exception as e:
    raise gamry_error_decoder(e)

client.PumpEvents(1)

#Close file
f.close()
input("Press Enter to close")
