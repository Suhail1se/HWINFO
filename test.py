import psutil
import time
import wmi

def get_cpu_temperature():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
        # Convert the temperature to Celsius
        temperature = temperature_info.CurrentTemperature
        return (temperature / 10.0) - 273.15
    except:
        return None

while True:
    CPUTemp = get_cpu_temperature()
    CPULOAD = psutil.cpu_percent()
    if CPUTemp is not None:
        print(f"CPU Temperature : {CPUTemp:.2f} °C - CPU Load : {CPULOAD:.2f} %")
    else:
        print(f"CPU Temperature : N/A - CPU Load : {CPULOAD:.2f} %")
    time.sleep(1)
