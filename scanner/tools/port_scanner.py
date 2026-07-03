import socket

def scan_ports(ip_address):
    open_ports = []
    common_ports = {
        21: 'FTP', 22: 'SSH', 25: 'SMTP', 80: 'HTTP',
        110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 3306: 'MySQL',
        8080: 'HTTP-alt'
    }
    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(f"{port} ({service})")
        sock.close()
    return open_ports