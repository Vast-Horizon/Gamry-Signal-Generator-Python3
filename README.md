# Gamry-Signal-Generator-Python3
![image](https://user-images.githubusercontent.com/50966363/177796983-56907dad-51e0-4ef4-b0f8-3a599150b8f7.png)

Gamry Signal Generator controls Interface5000E to output certain signals.\
Main program: GamrySignalMainCode.py\
UI file: projectui.ui

Other examples:\
RampPulse.py reads from a data file that has 1001 voltages data points(from 0V to 2V, straight back to 0 at the end). By default, RampPulse.py runs three cycles, with a 0.0001 seconds gap between each of the data points. RampPulse.py also saves raw data the potentiostat detected and polts a graph, as the demo1.jpg shows.\
sineWave.py is a separated, additional example that can generate a continuous sine wave.


The technologies used in this project:\
Gamry Echem Toolkit, Python 3, comtypes, Qt Designer and PyQt6\
The potentiostat being used during development was INTERFACE 5000E.

Use pip in your terminal to install following packages:\
pip install comtypes PyQt6 pyqtgraph numpy matplotlib

---
How to use:

Hardware Connection:\
Connect the Gamry potentiostat to your computer via USB.\
Leads: Green lead is positive. Red lead is negative. Blue lead is positive sensor. Orange lead is negative sensor.\
For two terminal object, for example, a typical battery, connect the green and blue leads to its positive terminal, and the red, white, and orange leads to the negative terminal.

Please keep the main program, the UI file, and img folder under a same directory.

Signal file should only be a single list of data.

Amp means multiply each points in the signal file to a set number; Amp = 1 means original signal./
Note that the device limit is 5A. For example, if your signal has a peak of 2.6, and you set the amp to 2, the program will NOT run since 2.6*2>5.

Output directory and file naming:\
Main Directory  = Program Directory + Model\
Sub Directory = Temperature + Condition\
File Name = Test Number + ID + Condition + Temperature + mmddyy + .csv

Output Columns from 1st to 4th respectively are:\
Time[s]	 Sampling Time[s]	 Input Signal	 Measur. V[V]	 Measur. I[A]

Use the radio button to switch between galvanostat mode and potentiostat mode.\
Click Test button to Run

You can set a default path to a data file here so you don't need to click Select Input Signal File everytime when you lunch the program
![image](https://user-images.githubusercontent.com/50966363/187491335-70b2b84c-f6e0-47fc-b146-0a12f8d2bf31.png)

Gamry Echem Toolkit Info:
https://www.gamry.com/support-2/software/echem-toolkit-basic-dc-and-ac/

---
New UI Ver.
![image](https://user-images.githubusercontent.com/50966363/187779302-34cef4b0-0e1f-4be6-964a-b860a8e295da.png)

Old UI Ver.\
![demo1](https://user-images.githubusercontent.com/50966363/177796481-0845cb86-bb3e-44d8-9c39-c82020d270a4.jpg)

Output Reading, from an external oscilloscope:\
![image](https://user-images.githubusercontent.com/50966363/177848081-875f893b-4d66-4358-8d7f-26bdc7fc9ee3.png)

IMPORTANT UPDATE NOTE :
A much more capable software with a brand new user interface is under development in GamrySignal_NewUIVersion folder. Stay Tuned.
---
(8/18/2022)\
The project now has a separated UI file. GamrySignalMainCode.py loads the ui file and link functionalities to it. Please put them under the same directory.\
For each run, the program save 5 columns of data(time + sampling time(element 0) + input signal + elements 1 and 3), then plots them vs time to the window.\
Comment out item = [item[i] for i in (0,1,3)] in GamrySignalMainCode.py to save all columns(elements).\
![image](https://user-images.githubusercontent.com/50966363/185494321-f042c8d9-eeef-4738-8043-bb86a30c8281.png)\
Note that GamrySignalMainCode.py is set to galvanostat mode and it reads current signal by default. Simply uncheck the radio button to switch to potentiostat mode if you wish.

---
(8/15/2022)\
IMPORTANT UPDATE NOTE :
A much more capable software with a brand new user interface is under development. Stay Tuned.
![image](https://user-images.githubusercontent.com/50966363/184974577-ea0c0098-b655-493e-be38-58d4c315b21f.png)

