import ttkbootstrap as tb
from ttkbootstrap.constants import *
import threading
import time
import collections
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from modules.cpu import get_cpu_usage
from modules.ram import get_ram_usage
from modules.disk import get_disk_usage
from modules.network import get_network_stats
from modules.config import *

class SystemHealthDashboard(tb.Window):
    def __init__(self):
        super().__init__(themename="cyborg")
        self.title("System Health Dashboard")
        self.geometry("800x500")
        self.resizable(False, False)

        # Data history for charts
        self.cpu_history = collections.deque([0] * HISTORY_LENGTH, maxlen=HISTORY_LENGTH)
        self.ram_history = collections.deque([0] * HISTORY_LENGTH, maxlen=HISTORY_LENGTH)
        self.disk_history = collections.deque([0] * HISTORY_LENGTH, maxlen=HISTORY_LENGTH)

        # Title
        tb.Label(
            self,
            text="🖥 System Health Dashboard",
            font=("Segoe UI", 20, "bold"),
            bootstyle=PRIMARY
        ).pack(pady=10)

        # Stats frame
        stats_frame = tb.Frame(self, padding=10)
        stats_frame.pack(fill=X)

        self.cpu_label = tb.Label(stats_frame, text="CPU Usage: --%", font=("Segoe UI", 12), bootstyle=PRIMARY)
        self.cpu_label.grid(row=0, column=0, sticky=W, pady=5)

        self.ram_label = tb.Label(stats_frame, text="RAM Usage: --%", font=("Segoe UI", 12), bootstyle=INFO)
        self.ram_label.grid(row=1, column=0, sticky=W, pady=5)

        self.disk_label = tb.Label(stats_frame, text="Disk Usage: --%", font=("Segoe UI", 12), bootstyle=WARNING)
        self.disk_label.grid(row=2, column=0, sticky=W, pady=5)

        self.net_label = tb.Label(stats_frame, text="Network: --", font=("Segoe UI", 12))
        self.net_label.grid(row=3, column=0, sticky=W, pady=5)

        # Refresh button (uses pack to avoid geometry conflict)
        tb.Button(
            self,
            text="🔄 Refresh Now",
            bootstyle=SUCCESS,
            command=self.update_stats
        ).pack(pady=(0, 12))

        # Chart frame
        chart_frame = tb.Frame(self, padding=10)
        chart_frame.pack(fill=BOTH, expand=True)

        self.fig, self.axes = plt.subplots(3, 1, figsize=(7, 5), dpi=100)
        self.fig.tight_layout(pad=2.0)

        chart_styles = [
            {"title": "CPU Usage (%)", "color": "lime"},
            {"title": "RAM Usage (%)", "color": "deepskyblue"},
            {"title": "Disk Usage (%)", "color": "orange"}
        ]

        self.charts = []
        for ax, history, style in zip(
            self.axes,
            [self.cpu_history, self.ram_history, self.disk_history],
            chart_styles
        ):
            ax.set_ylim(0, 100)
            line, = ax.plot(history, color=style["color"], linewidth=2)
            ax.set_title(style["title"], fontsize=10, color=style["color"], pad=5, weight="bold")
            ax.tick_params(colors="white")
            ax.set_facecolor("#222")
            ax.grid(True, linestyle="--", color="#444", alpha=0.5)
            ax.text(0.02, 0.85, style["title"].split()[0], transform=ax.transAxes,
                    fontsize=9, fontweight="bold", color=style["color"], alpha=0.7)
            self.charts.append({"ax": ax, "data": history, "line": line})

        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        # Auto-refresh thread
        threading.Thread(target=self.auto_refresh, daemon=True).start()

    def update_stats(self):
        cpu = get_cpu_usage()
        ram = get_ram_usage()
        disk = get_disk_usage()
        net = get_network_stats()

        self.cpu_label.config(text=f"CPU Usage: {cpu}%",
                              bootstyle=self.get_usage_style(cpu, CPU_WARN, CPU_CRIT, PRIMARY))
        self.ram_label.config(text=f"RAM Usage: {ram}%",
                              bootstyle=self.get_usage_style(ram, RAM_WARN, RAM_CRIT, INFO))
        self.disk_label.config(text=f"Disk Usage: {disk}%",
                               bootstyle=self.get_usage_style(disk, DISK_WARN, DISK_CRIT, WARNING))
        self.net_label.config(text=f"Network: {net}")

        # Update histories
        self.cpu_history.append(cpu)
        self.ram_history.append(ram)
        self.disk_history.append(disk)

        # Refresh chart lines
        for chart in self.charts:
            chart["line"].set_ydata(chart["data"])
            chart["line"].set_xdata(range(len(chart["data"])))
            chart["ax"].relim()
            chart["ax"].autoscale_view()

        self.canvas.draw()

    def auto_refresh(self):
        while True:
            self.update_stats()
            time.sleep(REFRESH_INTERVAL)

    @staticmethod
    def get_usage_style(value, warn, crit, base_style):
        if value >= crit:
            return DANGER
        elif value >= warn:
            return WARNING
        return base_style

if __name__ == "__main__":
    app = SystemHealthDashboard()
    app.mainloop()

