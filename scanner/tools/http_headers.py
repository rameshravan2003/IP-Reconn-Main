import requests

def get_http_headers(domain):
    """
    Fetches HTTP headers from a domain, trying HTTPS first, then HTTP.
    """
    # Set a common user-agent to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Try connecting via HTTPS first
    try:
        url = f"https://{domain}"
        response = requests.get(url, headers=headers, timeout=4, allow_redirects=True)
        response.raise_for_status() # Raise an exception for bad status codes
        
        # Return the final URL, status code, and all headers
        return {
            'final_url': response.url,
            'status_code': response.status_code,
            'headers': dict(response.headers)
        }
    except requests.exceptions.RequestException:
        # If HTTPS fails, try HTTP
        try:
            url = f"http://{domain}"
            response = requests.get(url, headers=headers, timeout=4, allow_redirects=True)
            response.raise_for_status()

            return {
                'final_url': response.url,
                'status_code': response.status_code,
                'headers': dict(response.headers)
            }
        except requests.exceptions.RequestException as e:
            return {'error': f'Could not retrieve HTTP headers: {e}'}