from osst import *

def main():
    print("=" * 50)
    print("📊 Operating System Story Teller (OSST)")
    print("=" * 50)

    system_data = get_system_resources()
    print_system_resources(system_data)

    network_data = get_network_info()
    print_network_info(network_data)

    services_data = get_active_services()
    print_services_info(services_data)

if __name__ == "__main__":
    main()
