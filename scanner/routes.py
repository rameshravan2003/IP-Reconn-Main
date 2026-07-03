import socket
import os
from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, render_template, current_app, request
from scanner.forms import TargetForm
from scanner.tools import geolocation, dns_lookup, whois_lookup, port_scanner, ssl_info, blacklist, http_headers, subdomain_scanner

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = TargetForm()
    if form.validate_on_submit():
        target = form.target.data
        results = {'target': target}

        try:
            ip_address = socket.gethostbyname(target)
            results['ip_address'] = ip_address
        except socket.gaierror:
            return render_template('index.html', form=form, error="Invalid Domain or IP Address.")

        is_ip = all(c in '0123456789.' for c in target)
        abuseipdb_key = current_app.config['ABUSEIPDB_API_KEY']
        
        with ThreadPoolExecutor() as executor:
            geo_future = executor.submit(geolocation.get_geolocation, ip_address)
            ports_future = executor.submit(port_scanner.scan_ports, ip_address)
            dns_future = executor.submit(dns_lookup.get_dns_records, target)
            whois_future = executor.submit(whois_lookup.get_whois_info, target)
            blacklist_future = executor.submit(blacklist.check_blacklist, ip_address, abuseipdb_key)
            headers_future = executor.submit(http_headers.get_http_headers, target)
            
            ssl_future = None
            subdomain_future = None
            if not is_ip:
                ssl_future = executor.submit(ssl_info.get_ssl_info, target)
                subdomain_future = executor.submit(subdomain_scanner.find_subdomains, target)

            results['geo'] = geo_future.result()
            results['ports'] = ports_future.result()
            results['dns'] = dns_future.result()
            results['whois'] = whois_future.result()
            results['blacklist'] = blacklist_future.result()
            results['headers'] = headers_future.result()
            
            if ssl_future:
                results['ssl'] = ssl_future.result()
            else:
                results['ssl'] = {'error': 'SSL check does not apply to IP addresses.'}

            if subdomain_future:
                results['subdomains'] = subdomain_future.result()
            else:
                results['subdomains'] = []
        
        return render_template('results.html', results=results)

    return render_template('index.html', form=form)

@main.route('/analyzer')
def analyzer():
    """Renders the live traffic analyzer page."""
    return render_template('analyzer.html')

@main.route('/get_traffic')
def get_traffic():
    """Reads the traffic log and returns filtered content."""
    # Get the filter from the URL query parameter (e.g., ?filter=google.com)
    filter_text = request.args.get('filter', '').strip()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_FILE = os.path.join(BASE_DIR, "traffic.log")
    
    try:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
            
            # If a filter is provided, keep only the lines that contain it
            if filter_text:
                filtered_lines = [line for line in lines if filter_text in line]
            else:
                filtered_lines = lines

            latest_lines = filtered_lines[-50:]
            latest_lines.reverse()
        return {"traffic": "".join(latest_lines)}
    except FileNotFoundError:
        return {"traffic": "Traffic log not found. Is the analyzer script running?"}