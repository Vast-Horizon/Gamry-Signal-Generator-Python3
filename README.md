# Gamry-Signal-Generator-Python3
![image](https://user-images.githubusercontent.com/50966363/177796983-56907dad-51e0-4ef4-b0f8-3a599150b8f7.png)

Connect your Gamry potentiostat to your computer.\
Connect the green and blue leads to the positive terminal, and the red, white, and orange leads to the negative terminal.\
The program tells the potentiostat to output a certain signal. sineWave.py generates a continuous sine wave. RampPulse.py reads from a data file that has 1001 voltages data points(from 0V to 2V, straight back to 0 at the end). By default, RampPulse.py runs three cycles, with a 0.0001 seconds gap between each of the data points. RampPulse.py also saves raw data the potentiostat detected and polts a graph, as the demo1.jpg shows.

The technologies used in this project are Gamry Echem Toolkit, Python 3, comtypes. The potentiostat being used during the development is INTERFACE 5000E.

use pip install comtypes in cmd to install the COM package\
Gamry Echem Toolkit:
https://www.gamry.com/support-2/software/echem-toolkit-basic-dc-and-ac/

![demo1](https://user-images.githubusercontent.com/50966363/177796481-0845cb86-bb3e-44d8-9c39-c82020d270a4.jpg)


Output Reading, from an external oscilloscope
![d17c2ebf7c0110002ff289c568eb1cf](https://user-images.githubusercontent.com/50966363/177798855-7f349cc8-51e3-4078-9710-b901fba64af1.jpg)
