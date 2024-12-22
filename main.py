from scanner.dns_enum import dns_enum

print("PRESS CORRESPONDING NUMBER TO SELECT OPTION \n 1. Enumerate DNS Records")
option = input("Enter option: ")

match option:
    case "1":
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

