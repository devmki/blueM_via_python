def read_and_write_ALL(filepath,time_frame, time_step = None):
    """
    Read and write the BlueM.Sim ALL file.
    The function will read the file, change the time frame and write it back to the file.
    Optionally, the time step can be changed as well.
    """
    try:
        all_data = None
        # Read the file
        with open(filepath, 'r', encoding='ANSI') as file:
            all_data = file.readlines()
            for i, line in enumerate(all_data):
                if ' SimBeginn - SimEnde ............:' in line:
                    all_data[i] = f' SimBeginn - SimEnde ............: {time_frame}\n'
                elif ' Zeitschrittlaenge [min] ........:' in line:
                    if isinstance(time_step, (float, int)):
                        all_data[i] = f' Zeitschrittlaenge [min] ........: {time_step / 60.0}\n'

        # Write back to the file
        with open(filepath, 'w', encoding='ANSI') as file:
            for line in all_data:
                file.write(f'{line}')

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing the file '{filepath}'.")
    except UnicodeDecodeError:
        print(f"Error: Failed to decode the file '{filepath}' with the specified encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
