# Formatting and printing results for CLI or JSON export

def print_system_resources(sys_data):
    print("=== System Resources ===")
    print(f"CPU Cores: {sys_data['cpu_cores']}")
    print(f"Total RAM: {sys_data['total_ram_gb']:.2f} GB")
    print(f"Total Disk Space: {sys_data['total_disk_gb']:.2f} GB")
