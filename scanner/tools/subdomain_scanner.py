import socket
# This import was missing
import concurrent.futures

# A small list of common subdomains to check for.
# For a more powerful tool, this list could be read from a large text file.
COMMON_SUBDOMAINS = [
    'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'ns2',
    'admin', 'api', 'dev', 'test', 'blog', 'shop', 'staging', 'support'
]

def find_subdomains(domain):
    """
    Finds existing subdomains for a given domain using a wordlist.
    """
    found_subdomains = []

    def check_subdomain(subdomain):
        """Helper function to check a single subdomain."""
        full_domain = f"{subdomain}.{domain}"
        try:
            # If gethostbyname succeeds, the subdomain exists.
            socket.gethostbyname(full_domain)
            return full_domain
        except socket.error:
            # If it fails, the subdomain does not exist.
            return None

    # Use ThreadPoolExecutor to check subdomains concurrently for speed
    # We now call it with concurrent.futures.ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        # Map the check_subdomain function to each word in our list
        future_to_subdomain = {executor.submit(check_subdomain, sub): sub for sub in COMMON_SUBDOMAINS}
        for future in concurrent.futures.as_completed(future_to_subdomain):
            result = future.result()
            if result:
                found_subdomains.append(result)
    
    return sorted(found_subdomains)