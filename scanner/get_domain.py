import socket

def get_domain_name(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)
        return domain_name[0]  # The first element contains the domain name
    except socket.herror:
        return f"Error: Unable to resolve the IP address '{ip_address}'"