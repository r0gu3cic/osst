# import psutil
# import socket


# def get_network_interfaces():
#     interfaces = psutil.net_if_addrs()
#     network_interfaces = {}

#     for iface_name, iface_addrs in interfaces.items():
#         for addr in iface_addrs:
#             if addr.family == socket.AF_INET and not addr.address.startswith("127."):
#                 network_interfaces[iface_name] = addr.address
#     return network_interfaces


# def get_open_ports():
#     open_ports = set()
#     connections = psutil.net_connections(kind="inet")

#     for conn in connections:
#         if conn.status == psutil.CONN_LISTEN:
#             ip, port = conn.laddr
#             if not ip.startswith("127.") and ip != "::1":
#                 open_ports.add((ip, port))

#     return sorted(open_ports)
