import dns.resolver

def get_dns_records(domain):
    """
    Gets common DNS records for a domain using a specific, reliable resolver.
    """
    # Create a resolver instance
    resolver = dns.resolver.Resolver()
    
    # Configure it to use a reliable public DNS server (e.g., Google's)
    resolver.nameservers = ['8.8.8.8']
    resolver.lifetime = 2.0
    resolver.timeout = 2.0

    records = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    for rtype in record_types:
        try:
            # Use our custom resolver instance to perform the query
            answers = resolver.resolve(domain, rtype)
            records[rtype] = [str(r.to_text()) for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
            # Also catch the Timeout exception here
            records[rtype] = []
    return records