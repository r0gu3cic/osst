# Formatting and printing results for CLI or JSON export

def print_system_resources(sys_data):
    print("\n🖥️ System Information:")
    print(f"CPU Cores: {sys_data['cpu_cores']}")
    print(f"Total RAM: {sys_data['total_ram_gb']:.2f} GB")
    print(f"Total Disk Space: {sys_data['total_disk_gb']:.2f} GB")

def print_network_info(net_data):
    print("\n🌐 Network Information:")
    
    if net_data['interfaces']:
        print("Network Interfaces and IP Addresses:")
        for iface, ip in net_data['interfaces'].items():
            print(f"- {iface}: {ip}")
    else:
        print("No active network interfaces found.")

    if net_data['open_ports']:
        print("\nOpen Listening Ports (non-loopback):")
        for ip, port in net_data['open_ports']:
            print(f"- {ip}:{port}")
    else:
        print("No open listening ports found.")
