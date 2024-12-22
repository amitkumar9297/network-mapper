import socket

def specific_port_scan(target, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def scan_ports(target, port_range):
    open_ports = []
    for port in range(1, port_range):  
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  
            result = s.connect_ex((target, port))  # Try connecting to the port
            if result == 0: 
                open_ports.append(port)
    return open_ports


def port_scan():
    print("PRESS CORRESPONDING NUMBER TO SELECT OPTION \n1. Scan All Ports \n2. Scan First 1024 Ports \n3. specific port range 1 to _-_-_-_- \n4. Scan Specific Ports")
    option = input("Enter option: ")

    print("Enter target IP address or Domain name to scan ports")
    target = input("Enter target: ")

    match option:
        case "1":
            open_ports = scan_ports(target, 65536)
            print(f"Open ports: {open_ports}")
            return
        case "2":
            open_ports = scan_ports(target, 1024)
            print(f"Open ports: {open_ports}")
            return 
        case "3":
            port_range = int(input("Enter port range to scan (1 to _-_-_-_-): "))
            open_ports = scan_ports(target, port_range)
            print(f"Open ports: {open_ports}")
        case "4":
            ports = input("Enter comma separated ports to scan: ")
            ports = [int(port) for port in ports.split(",")]
            open_ports = specific_port_scan(target, ports)
            print(f"Open ports: {open_ports}")
            return