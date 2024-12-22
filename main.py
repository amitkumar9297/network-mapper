from scanner.dns_enum import dns_enum
from scanner.port_scan import port_scan
from scanner.traceroute import traceroute
from scanner.get_ip_address import get_ip_address
from scanner.get_domain import get_domain_name
from scanner.who_is import get_whois_info
from scanner.os_detection import os_fingerprinting

print("PRESS CORRESPONDING NUMBER TO SELECT OPTION \n1. Scan Ports \n2. Enumerate DNS Records \n3. Traceroute \n4. Get IP Address of Domain \n5. Get Domain of IP Address \n6. Get Whois Information \n7. O/S Detection \n8. Firewall/Filter Detection \n ---> Press /q to quit")
option = input("Enter option: ")

match option:
    case "1":
        port_scan()

    case "2":
        print("PLEASE ENTER DOMAIN NAME TO ENUMERATE DNS RECORDS")
        domain = input("Enter domain name: ")
        result = dns_enum(domain)
        
        for record_type, values in result.items():
            print(f"--- {record_type} Records ---")
            if values:
                for idx, value in enumerate(values, 1):
                    print(f"{idx}. {value}")
            else:
                print("No records found.")
            print("-" * 30)
    
    case "3":
        target = input("Enter target IP address or Domain name to traceroute: ")
        traceroute(target)
    case "4":
        domain = input("Enter domain name: ")
        ip_address = get_ip_address(domain)
        print(f"IP address: {ip_address}")
    case "5":
        ip_address = input("Enter IP address: ")
        domain = get_domain_name(ip_address)
        print(f"Domain name: {domain}")
    case "6":
        domain = input("Enter domain name: ")
        whois_info = get_whois_info(domain)
        print(whois_info)
    case "7":
        target = input("Enter target IP address or Domain for O/S detection: ")
        os_fingerprinting(target)

