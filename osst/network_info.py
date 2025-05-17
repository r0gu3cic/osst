import psutil
import socket


def get_network_info():
    """
    Returns network info as a dict with:
    - interfaces: dict of interface_name -> IPv4 address (ignoring loopback)
    - open_ports: list of tuples (ip, port) where the port is listening on non-loopback addresses
    """
    interfaces = psutil.net_if_addrs()
    result_interfaces = {}

    for iface_name, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                result_interfaces[iface_name] = addr.address

    open_ports = set()
    connections = psutil.net_connections(kind="inet")

    for conn in connections:
        if conn.status == psutil.CONN_LISTEN:
            ip, port = conn.laddr

            # Skip IPv6 addresses and loopback
            if ":" in ip or ip == "::" or ip == "::1":
                continue

            if not ip.startswith("127."):
                open_ports.add((ip, port))

    return {"interfaces": result_interfaces, "open_ports": sorted(open_ports)}
