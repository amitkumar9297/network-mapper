import nmap
import socket

def firewall_detection(target):
    # Resolve domain name to IP if input is a domain name
    if not is_ip(target):
        try:
            target = socket.gethostbyname(target)
        except socket.gaierror:
            print("Invalid domain name.")
            return
    
    # Perform firewall detection using nmap
    nm = nmap.PortScanner()
    print("Scanning start.........")
    nm.scan(target, arguments='-sA')  # -sA for ACK scan to detect firewall
    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"Firewall state: {nm[host].state()}")


def is_ip(address):
    try:
        socket.inet_aton(address)  # Check if it's a valid IPv4 address
        return True
    except socket.error:
        return False


