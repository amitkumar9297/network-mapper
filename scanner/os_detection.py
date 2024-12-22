import nmap
import socket

def os_fingerprinting(target):
    # Resolve domain name to IP if input is a domain name
    if not is_ip(target):
        try:
            target = socket.gethostbyname(target)
        except socket.gaierror:
            print("Invalid domain name.")
            return
    
    # Perform OS fingerprinting with the resolved IP address
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-O')
    
    if 'osmatch' in nm[target]:
        print(f"OS Match: {nm[target]['osmatch']}")
    else:
        print("No OS information available.")

# Helper function to check if the input is an IP address
def is_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False
