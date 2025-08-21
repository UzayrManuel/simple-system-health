import tkinter as tk
import psutil
import threading
import time

# ---------- Data Collection ----------
def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = "Online" if psutil.net_io_counters().bytes_sent > 0 else "Offline"
    return cpu, mem, disk, net

# ---------- UI Update Loop ----------
def update_stats():
    while True:
        cpu, mem, disk, net = get_stats()
        cpu_label.config(text=f"CPU Usage: {cpu}%", fg=color_for(cpu))
        mem_label.config(text=f"Memory Usage: {mem}%", fg=color_for(mem))
        disk_label.config(text=f"Disk Usage: {disk}%", fg=color_for(disk))
        net_label.config(text=f"Network: {net}", fg="green" if net == "Online" else "red")
        time.sleep(2)

def color_for(value):
    if value < 60:
        return "green"
    elif value < 85:
        return "orange"
    return "red"

# ---------- Main Window ----------
root = tk.Tk()
root.title("System Health Dashboard")
root.geometry("300x200")
root.resizable(False, False)

title_label = tk.Label(root, text="System Health Dashboard", font=("Segoe UI", 14, "bold"))
title_label.pack(pady=10)

cpu_label = tk.Label(root, font=("Segoe UI", 12))
cpu_label.pack()
mem_label = tk.Label(root, font=("Segoe UI", 12))
mem_label.pack()
disk_label = tk.Label(root, font=("Segoe UI", 12))
disk_label.pack()
net_label = tk.Label(root, font=("Segoe UI", 12))
net_label.pack(pady=5)

# Run stats updater in a separate thread so the UI stays responsive
threading.Thread(target=update_stats, daemon=True).start()

root.mainloop()