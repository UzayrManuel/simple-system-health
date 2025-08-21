import psutil

def get_network_io():
    """Return network I/O in KB sent and received."""
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent // 1024, net_io.bytes_recv // 1024