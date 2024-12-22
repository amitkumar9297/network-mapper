import dns.resolver

def dns_enum(domain):
    """
    Enumerate DNS records for a given domain.
    """
    record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME', 'SOA']
    records = {}

    for record_type in record_types:
        try:
            records[record_type] = [str(r) for r in dns.resolver.resolve(domain, record_type)]
        except Exception as e:
            records[record_type] = []  # No records or query failed

    return records

# Example usage
if __name__ == "__main__":
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

