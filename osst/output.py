# Formatting and printing results for CLI or JSON export


def print_system_resources(system_data):
    print("\n[SYS] System Information:")
    print(f"CPU Cores: {system_data['cpu_cores']}")
    print(f"Total RAM: {system_data['total_ram_gb']:.2f} GB")
    print(f"Total Disk Space: {system_data['total_disk_gb']:.2f} GB")


def print_network_info(net_data):
    print("\n[NET] Network Information:")

    if net_data["interfaces"]:
        print("Network Interfaces and IP Addresses:")
        for iface, ip in net_data["interfaces"].items():
            print(f"- {iface}: {ip}")
    else:
        print("No active network interfaces found.")

    if net_data["open_ports"]:
        print("\nOpen Listening Ports (non-loopback):")
        for ip, port in net_data["open_ports"]:
            print(f"- {ip}:{port}")
    else:
        print("\n[NET] No open listening ports found.")


def print_services_info(services):
    """
    Nicely prints the list of active services.
    """
    if not services:
        print("\n[SRV] No relevant active services found.")
    else:
        print("\n[SRV] Active services (excluding system defaults):")
        for svc in services:
            print(f"- {svc}")
