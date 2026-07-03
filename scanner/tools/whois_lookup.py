import whois
from ipwhois import IPWhois
from ipwhois.exceptions import IPDefinedError
import socket

def get_whois_info(target):
    """
    Performs a WHOIS lookup on either a domain name or an IP address.
    """
    # Determine if the target is an IP address
    try:
        socket.inet_aton(target)
        is_ip = True
    except socket.error:
        is_ip = False

    try:
        if is_ip:
            # If it's an IP, use the ipwhois library
            obj = IPWhois(target)
            results = obj.lookup_whois()
            return {
                'asn_description': results.get('asn_description'),
                'nets': results.get('nets', [{}])[0].get('description')
            }
        else:
            # If it's a domain, use the python-whois library
            w = whois.whois(target)
            
            # This function handles cases where a date might be a list
            def get_date(date_data):
                if isinstance(date_data, list):
                    return date_data[0] # Take the first date from the list
                return date_data

            # Check for empty or failed lookups
            if not w.registrar:
                return {'error': 'WHOIS lookup failed. No registrar data found.'}
                
            return {
                'registrar': w.registrar,
                'creation_date': get_date(w.creation_date),
                'expiration_date': get_date(w.expiration_date),
                'name_servers': w.name_servers
            }
    except whois.parser.PywhoisError as e:
        # Catch specific parsing errors from the whois library
        return {'error': f"WHOIS data could not be parsed: {e}"}
    except Exception as e:
        # Catch all other errors, including network timeouts
        return {'error': f"An error occurred: {e}"}