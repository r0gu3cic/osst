# Entry point – CLI interface

from osst import system_info

def main():
    print("[OSST] Starting system inspection...\n")

    sys_data = system_info.get_system_resources()

    print("=== System Resources ===")
    print(f"CPU Cores: {sys_data['cpu_cores']}")
    print(f"Total RAM: {sys_data['total_ram_gb']:.2f} GB")
    print(f"Total Disk Space: {sys_data['total_disk_gb']:.2f} GB")

if __name__ == "__main__":
    main()
