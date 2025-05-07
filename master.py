from glob import glob
from os import getcwd
from sys import exit
import clr


import read_and_write_bluem_files as rw_bluem
import simulate_blueM as sb

####################################################################################
# USER SETTINGS
####################################################################################
#BlueM.Sim DLLs 
# The DLLs are located in the BlueM installation folder
# adjust the paths accordingly
blueM_adapter_path = 'path_to/BlueM.DllAdapter.dll'
blueM_sim_path = 'path_to/BlueM.Sim.dll'

#Simulation dates
# just ensure it is a list of strings with the correct format
dates = ['01.01.1980 00:00 - 31.12.2000 00:00', #period 1
         '01.01.2001 00:00 - 31.12.2010 00:00'] #period 2 etc etc.

#search all ALL-Files
# adjust to your folder structure
# The script will search for all files with the extension .ALL in the given path and 
# its subdirectories
path = getcwd() 
files = glob(path + '/**/*.ALL', recursive = True)

####################################################################################
#OPTIONAL SETTINGS
####################################################################################
#Time step in seconds
# If not set, the time step will be read from the ALL file
TIME_STEP = None
####################################################################################

#load the BlueM Adapter DLL 
clr.AddReference(blueM_adapter_path)

#Import from the BlueM Adapter DLL
from BlueM.DllAdapter import BlueM_EngineDotNetAccess

#connect to the BlueM.Sim DLL
bluem_dll = BlueM_EngineDotNetAccess(blueM_sim_path)

# make a dictionary with the time frames
time_framedict = {str(i + 1): dates[i] for i in range(len(dates))}

#which time frame is considered?
for i in range(len(dates)):
    print(f'{i + 1}: {dates[i]}')
user_input = input('which time frame are we using? ')

try:
    time_frame = time_framedict[user_input]
except KeyError:
    print(f"Invalid selection: '{user_input}'. Please choose a valid time frame from the list.")
    exit(1)  # Exit the program if the input is invalid1

#how many all files were found?
number_of_files = len(files)

#simulate the BlueM.Sim model with the given files
i = 0
for file in files:
    i += 1
    # Write correct time frame into ALL-Files
    print(f'processing ALL {i}/{number_of_files}')
    rw_bluem.read_and_write_ALL(file, time_frame)  # [s]
    # Simulate
    sb.simulate_bluem(file, bluem_dll)
