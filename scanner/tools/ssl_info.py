import ssl
import socket
from datetime import datetime

def get_ssl_info(hostname):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443), timeout=2) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z').isoformat()
                valid_until = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z').isoformat()
                return {
                    'issuer': dict(x[0] for x in cert['issuer']),
                    'subject': dict(x[0] for x in cert['subject']),
                    'valid_from': valid_from,
                    'valid_until': valid_until
                }
    except (socket.gaierror, socket.timeout, ssl.SSLCertVerificationError, ConnectionRefusedError, OSError):
        return {'error': 'Could not retrieve SSL certificate. The site may not use HTTPS or is unreachable.'}