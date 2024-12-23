import GPUtil
import time
import os

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_info = []
            for gpu in gpus:
                name = gpu.name
                temperature = gpu.temperature if gpu.temperature is not None else "N/A"
                usage = gpu.load * 100 if gpu.load is not None else "N/A"
                gpu_info.append((name, temperature, usage))
            return gpu_info
        else:
            return [("N/A", "N/A", "N/A")]
    except Exception as e:
        return [(str(e), "N/A", "N/A")]

def clear_console():
    # Clear the console for better readability of output
    os.system('cls')

if __name__ == "__main__":
    while True:
        clear_console()  # Clear the console screen
        gpu_info = get_gpu_info()
        if isinstance(gpu_info, list):
            print("GPU Information:")
            for i, (name, temperature, usage_percent) in enumerate(gpu_info):
                temp_display = f"{temperature} °C" if temperature != "N/A" else "N/A"
                usage_display = f"{usage_percent:.2f}%" if usage_percent != "N/A" else "N/A"
                print(f"GPU {i} ({name}): Temperature: {temp_display}, Usage: {usage_display}")
        else:
            print("Error:", gpu_info)
        time.sleep(1)  # Wait for 1 second before updating
