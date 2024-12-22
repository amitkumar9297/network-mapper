from scanner.dns_enum import dns_enum
from scanner.port_scan import port_scan

print("PRESS CORRESPONDING NUMBER TO SELECT OPTION \n1. Scan Ports \n2. Enumerate DNS Records")
option = input("Enter option: ")

match option:
    case "1":
        port_scan()

    case "2":
        print("PLEASE ENTER DOMAIN NAME TO ENUMERATE DNS RECORDS")
        domain = input("Enter domain name: ")
        result = dns_enum(domain)
        
        # Pretty-print the result
        for record_type, values in result.items():
            print(f"--- {record_type} Records ---")
            if values:
                for idx, value in enumerate(values, 1):
                    print(f"{idx}. {value}")
            else:
                print("No records found.")
            print("-" * 30)

