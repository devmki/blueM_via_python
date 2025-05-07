from datetime import datetime
def simulate_bluem(file, bluem_dll):
    """
    Simulate the BlueM.Sim model with the given file.
    """
    print('Initalizing BlueM.Sim model')
    bluem_dll.Initialize(file)
    sim_end = bluem_dll.GetSimulationEndDate()
    sim_end = datetime.strptime(sim_end,'%Y%m%d %H:%M')

    print('Starting BlueM.Sim simulation')
    while datetime.strptime(bluem_dll.GetCurrentTime(),'%Y%m%d %H:%M') <= sim_end:
        print('Performing time step', datetime.strptime(bluem_dll.GetCurrentTime(),'%Y%m%d %H:%M'))
        bluem_dll.PerformTimeStep()
       
    bluem_dll.Finish()