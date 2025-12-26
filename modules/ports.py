import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 8080, 8443]

def scan_ports(target):
    open_ports = []
    for port in COMMON_PORTS:
        try:
            s = socket.socket()
            s.settimeout(0.7)
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
            s.close()
        except:
            continue
    return open_ports
