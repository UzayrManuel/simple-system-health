import psutil

RAM_WARN = 60
RAM_DANGER = 85

def get_ram_usage():
    """Return RAM usage as a percentage."""
    return psutil.virtual_memory().percent

def get_thresholds():
    return RAM_WARN, RAM_DANGER