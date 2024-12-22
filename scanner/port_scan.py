import socket
import nmap

def service_version_scan(target, scan_type):
    if not is_ip(target):
        try:
            target = socket.gethostbyname(target)
        except socket.gaierror:
            print("Invalid domain name.")
            return
    
    nm = nmap.PortScanner()
    
    # Determine scan type
    if scan_type == "first_1024":
        nm.scan(target, arguments='-sV')  # Default scan for first 1024 ports
    elif scan_type == "all_ports":
        nm.scan(target, arguments='-sV -p-')  # Scan all ports
    elif scan_type.startswith("specific_ports:"):
        ports = scan_type.split(":")[1]
        print("scanning start........")
        nm.scan(target, arguments=f'-sV -p {ports}')  # Scan specific ports
    
    # Process and display results
    for host in nm.all_hosts():
        print(f"\nHost: {host}")
        for proto in nm[host].all_protocols():
            print(f"  Protocol: {proto}")
            for port, details in nm[host][proto].items():
                service = details.get('name', 'Unknown')
                version = details.get('version', 'Unknown')
                print(f"    Port {port}: {service} {version}")

# Helper function to check if the input is an IP address
def is_ip(address):
    try:
        socket.inet_aton(address)  # Check if it's a valid IPv4 address
        return True
    except socket.error:
        return False






def specific_port_scan(target, ports):
    open_ports = []
    print("Scanning start........")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def scan_ports(target, port_range):
    open_ports = []
    print("Scanning start........")
    for port in range(1, port_range):  
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  
            result = s.connect_ex((target, port))  # Try connecting to the port
            if result == 0: 
                open_ports.append(port)
    return open_ports


def port_scan():
    print("PRESS CORRESPONDING NUMBER TO SELECT OPTION \n1. Scan All Ports \n2. Scan First 1024 Ports \n3. specific port range 1 to _-_-_-_- \n4. Scan Specific Ports \n5. service version detection")
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
        case "5":
            scan_type = input("Enter scan type (first_1024, all_ports, specific_ports:port1,port2,...): ")
            service_version_scan(target, scan_type)
            return