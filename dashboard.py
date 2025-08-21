# dashboard.py
import tkinter as tk
from tkinter import ttk
import psutil
import platform
import threading
import time

REFRESH_INTERVAL = 2000  # milliseconds

class SystemHealthDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Health Dashboard")
        self.geometry("400x250")
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self._build_ui()
        self.update_stats()

    def _build_ui(self):
        ttk.Label(self, text="🖥️ System Health Dashboard", font=("Segoe UI", 14, "bold")).pack(pady=5)

        self.cpu_var = tk.StringVar()
        self.ram_var = tk.StringVar()
        self.disk_var = tk.StringVar()
        self.net_var = tk.StringVar()

        for label, var in [
            ("CPU Usage:", self.cpu_var),
            ("RAM Usage:", self.ram_var),
            ("Disk Usage:", self.disk_var),
            ("Network I/O:", self.net_var),
        ]:
            frame = ttk.Frame(self)
            frame.pack(fill="x", padx=15, pady=4)
            ttk.Label(frame, text=label, width=15, anchor="w").pack(side="left")
            ttk.Label(frame, textvariable=var, anchor="w").pack(side="left")

        sys_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
        ttk.Label(self, text=sys_info, font=("Segoe UI", 9, "italic")).pack(side="bottom", pady=5)

    def update_stats(self):
        self.cpu_var.set(f"{psutil.cpu_percent()}%")
        self.ram_var.set(f"{psutil.virtual_memory().percent}%")
        self.disk_var.set(f"{psutil.disk_usage('/').percent}%")
        net_io = psutil.net_io_counters()
        self.net_var.set(f"Sent: {net_io.bytes_sent // 1024} KB | Recv: {net_io.bytes_recv // 1024} KB")

        self.after(REFRESH_INTERVAL, self.update_stats)

if __name__ == "__main__":
    app = SystemHealthDashboard()
    app.mainloop()