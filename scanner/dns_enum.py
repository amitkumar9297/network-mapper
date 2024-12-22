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
            records[record_type] = [] 

    return records


