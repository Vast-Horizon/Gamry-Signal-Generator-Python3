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
import matplotlib.pyplot as plot
import time

GamryCOM=client.GetModule(['{BD962F0D-A990-4823-9CF5-284D1CDD9C6D}', 1, 0])
# Alternatively:
#GamryCOM=client.GetModule(r'C:\Program Files\Gamry Instruments\Framework 6\GamryCOM.exe')

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

    active = False
    print(len(dtaqsink.acquired_points))

    pstat.SetCell(GamryCOM.CellOff)
    time.sleep(1)
    pstat.Close()
    del connection
    gc.collect()
    return
###############################

devices=client.CreateObject('GamryCOM.GamryDeviceList')
print(devices.EnumSections())

pstat=client.CreateObject('GamryCOM.GamryPC6Pstat')
pstat.Init(devices.EnumSections()[0]) # grab first pstat

dtaqcpiv=client.CreateObject('GamryCOM.GamryDtaqCpiv')
dtaqcpiv.Init(pstat)

pstat.Open()
#======================
#Data points per period. Fs = 200 by default
Fs = 200 
#User Input
while True:
    try:
        
        Hz = int(input("Frequency of the sine wave in Hz: "))
        if Hz<=0:
            raise ValueError
            continue     
        
        Fs = int(input("Number of data samples per sine period(200 by default): "))
        while Fs<=0:
            print("Sorry. Please enter a positive integer.")
            Fs = int(input("Number of data samples: "))
        
        Amp = int(input("Amplitude in Volt: "))
    except ValueError:
        print("Sorry. Please enter a positive integer.")
        continue
    else:
        break

#SampleRate controls the output frequency.
#SampleRate is the time gap between each point in the list
a = 1./Fs
SampleRate = a/Hz

#Generate a list of 1Hz sine wave data points
t = np.arange(0, 1, 1/Fs)
F = 1
y = Amp*np.sin(2*np.pi*F*t)

#convert numpy array to list, as y-axis
signal = y.tolist() 
print("Number of Data Points: ", len(signal))

#Create a signal object then set it to pstat
SineSig=client.CreateObject('GamryCOM.GamrySignalArray')
SineSig.Init(pstat, -1, SampleRate, Fs, signal, GamryCOM.PstatMode)
pstat.SetSignal(SineSig)

#======================
#Start to output signal
pstat.SetCell(GamryCOM.CellOn)

dtaqsink = GamryDtaqEvents(dtaqcpiv)
#connection = client.GetEvents(dtaqcpiv, dtaqsink)

try:
    dtaqcpiv.Run(True)
    print("Running...")
    
except Exception as e:
    raise gamry_error_decoder(e)

client.PumpEvents(1)
#print(len(dtaqsink.acquired_points))

'''
while True:
    print(pstat.MeasureV())
    time.sleep(0.2)
    inp = input()
    if inp == "":
        break

'''
#Plot
plot.title('Sine wave')
plot.xlabel('Time(s)')
plot.ylabel('Voltage(V)')
x = np.arange(0, 1/Hz, (1/Hz)/Fs)
plot.plot(x, signal)
plot.show(block=False)
plot.show()

#Close
print("Terminating...")
#del connection
#gc.collect()
pstat.SetCell(GamryCOM.CellOff)
pstat.Close()
print("OFF")
