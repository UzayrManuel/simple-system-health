import psutil

DISK_WARN = 70
DISK_DANGER = 90

def get_disk_usage():
    """Return disk usage as a percentage for root ('/')."""
    return psutil.disk_usage('/').percent

def get_thresholds():
    return DISK_WARN, DISK_DANGER