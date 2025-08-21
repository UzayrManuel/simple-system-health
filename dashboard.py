import ttkbootstrap as tb
from ttkbootstrap.constants import *
import threading
import time

from modules.cpu import get_cpu_usage
from modules.ram import get_ram_usage
from modules.disk import get_disk_usage
from modules.network import get_network_stats


class SystemHealthDashboard(tb.Window):
    def __init__(self):
        super().__init__(themename="cyborg")  # Try "flatly" or "darkly" if you prefer
        self.title("System Health Dashboard")
        self.geometry("500x350")
        self.resizable(False, False)

        # Title
        tb.Label(
            self,
            text="🖥 System Health Dashboard",
            font=("Segoe UI", 18, "bold"),
            bootstyle=PRIMARY
        ).pack(pady=10)

        # Stats frame for clean layout
        stats_frame = tb.Frame(self, padding=10)
        stats_frame.pack(fill=BOTH, expand=True)

        # CPU
        self.cpu_label = tb.Label(stats_frame, text="CPU Usage: --%", font=("Segoe UI", 12))
        self.cpu_label.grid(row=0, column=0, sticky=W, pady=5)

        # RAM
        self.ram_label = tb.Label(stats_frame, text="RAM Usage: --%", font=("Segoe UI", 12))
        self.ram_label.grid(row=1, column=0, sticky=W, pady=5)

        # Disk
        self.disk_label = tb.Label(stats_frame, text="Disk Usage: --%", font=("Segoe UI", 12))
        self.disk_label.grid(row=2, column=0, sticky=W, pady=5)

        # Network
        self.net_label = tb.Label(stats_frame, text="Network: --", font=("Segoe UI", 12))
        self.net_label.grid(row=3, column=0, sticky=W, pady=5)

        # Refresh button
        tb.Button(
            self,
            text="🔄 Refresh Now",
            bootstyle=SUCCESS,
            command=self.update_stats
        ).pack(pady=10)

        # Background auto-refresh
        threading.Thread(target=self.auto_refresh, daemon=True).start()

    def update_stats(self):
        cpu = get_cpu_usage()
        ram = get_ram_usage()
        disk = get_disk_usage()
        net = get_network_stats()

        self.cpu_label.config(text=f"CPU Usage: {cpu}%")
        self.ram_label.config(text=f"RAM Usage: {ram}%")
        self.disk_label.config(text=f"Disk Usage: {disk}%")
        self.net_label.config(text=f"Network: {net}")

    def auto_refresh(self):
        while True:
            self.update_stats()
            time.sleep(5)


if __name__ == "__main__":
    app = SystemHealthDashboard()
    app.mainloop()