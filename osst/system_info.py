import psutil


def get_system_resources():
    """
    Returns basic system resource information:
    - Number of CPU cores
    - Total RAM in GB
    - Total disk space in GB
    """
    cpu_cores = psutil.cpu_count(logical=True)
    total_ram_gb = psutil.virtual_memory().total / (1024**3)
    total_disk_gb = psutil.disk_usage("/").total / (1024**3)

    return {
        "cpu_cores": cpu_cores,
        "total_ram_gb": total_ram_gb,
        "total_disk_gb": total_disk_gb,
    }
