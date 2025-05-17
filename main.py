# Entry point – CLI interface

from osst import system_info, network_info, output

def main():
    print("=" * 50)
    print("📊 Operating System Story Teller (OSST)")
    print("=" * 50)

    sys_data = system_info.get_system_resources()

    output.print_system_resources(sys_data)

    network_data = network_info.get_network_info()

    output.print_network_info(network_data)

if __name__ == "__main__":
    main()
