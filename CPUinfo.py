import psutil
import time
import os
import cpuinfo
import wmi

def clear_console():
    # Clear the console for better readability of output
    os.system('cls')

if __name__ == "__main__":
    cpu_info = cpuinfo.get_cpu_info()
    cpu_name = cpu_info['brand_raw']

    while True:
        clear_console()
        print(f"CPU Name  : {cpu_name}")
        print(f"CPU Usage : {psutil.cpu_percent():.2f} %")
        time.sleep(1)
