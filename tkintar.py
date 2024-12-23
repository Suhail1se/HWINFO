import GPUtil
import time
import os
import tkinter as tk

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

def update_gpu_info():
    gpu_info = get_gpu_info()
    info_text = "GPU Information:\n"
    for i, (name, temperature, usage_percent) in enumerate(gpu_info):
        temp_display = f"{temperature} °C" if temperature != "N/A" else "N/A"
        usage_display = f"{usage_percent:.2f}%" if usage_percent != "N/A" else "N/A"
        info_text += f"GPU {i} ({name}): Temperature: {temp_display}, Usage: {usage_display}\n"
    info_label.config(text=info_text)
    root.after(1000, update_gpu_info)  # Update every second

# Set up Tkinter window
root = tk.Tk()
root.title("GPU Monitor")
root.geometry("400x200")

info_label = tk.Label(root, text="", justify="left", font=("Helvetica", 12))
info_label.pack(padx=10, pady=10)

update_gpu_info()  # Initial call to start the loop

root.mainloop()
