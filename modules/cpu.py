import psutil

CPU_WARN = 50
CPU_DANGER = 80

def get_cpu_usage():
    """Return CPU usage as a percentage."""
    return psutil.cpu_percent()

def get_thresholds():
    """Return warning and danger thresholds."""
    return CPU_WARN, CPU_DANGER