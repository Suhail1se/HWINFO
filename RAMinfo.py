import time
import psutil
import os
import wmi

def clear_console():
    # Clear the console for better readability of output
    os.system('cls')

def get_memory_info():
    # Get basic RAM usage
    ram_usage = psutil.virtual_memory().percent
    ram_total = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB

    return ram_usage, ram_total
def get_memory_details():
    c = wmi.WMI()
    for memory in c.Win32_PhysicalMemory():
        print(f"Capacity: {int(memory.Capacity) / (1024 ** 3)} GB")
        print(f"Speed: {memory.Speed} MHz")


if __name__ == "__main__":
    print("RAM Usage Information")
    while True:     
        clear_console()
        get_memory_details()
        ram_usage, ram_total = get_memory_info()
        print(f"RAM Usage: {ram_usage} %")
        time.sleep(1)
