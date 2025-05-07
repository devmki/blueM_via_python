# BlueM.Sim and Python

This repo includes three scripts to run the BlueM.Sim DLL using Python. 

BlueM is a software package for hydrological simulation, data analysis and multi criteria optimizatzion. 
For more details refer to [BlueM Homepage](https://bluemodel.org/)


## simulate_blueM.py

The function in this script takes a file and the bluem_dll object and runs the actual BlueM.Sim simulation

## read_and_write_bluem_files.py

The function in this script reads the general settings file (ALL) of BlueM.Sim. It writes the simulation time frame (start date - end date) 
and the time step to the ALL file. If time step is not given, then the time step in the ALL file is kept.
This function is particularly useful if you want to run multiple BlueM.Sim model variants for the same time frame and with the same
time step. E.g. after solutions were selected and written by BlueM.Opt.

## master.py

This is the execution script. To run BlueM.Sim is required to be installed on your device. 
BlueM.Sim can be downloaded from the BlueM Website [download](https://downloads.bluemodel.org/?dir=BlueM.Win)

### How to run

The user must make settings in the USER SETTINGS section and optionally in the OPTIONAL SETTINGS.
Required settings are  
1. path to the BlueM.DllAdapter.dll
2. path to the BlueM.Sim.dll.
3. the time frames for simulations need to be defined.
4. the path and files variables should be adjusted to your folder structure.

Optional settings are defining a new time step, which will be written into the ALL files and used for the simulation.

**clr is used to load the BlueM.DllAdapter.dll, DO NOT pip install clr, use `pip install pythonnet`**
