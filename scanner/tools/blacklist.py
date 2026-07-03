import requests

# The function now accepts api_key as an argument
def check_blacklist(ip_address, api_key):
    """
    Checks an IP address against the AbuseIPDB blacklist.
    """
    # The API key is now passed in, so we don't need to look for it here.
    if not api_key:
        return {'error': 'AbuseIPDB API key was not provided.'}

    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=3)
        response.raise_for_status() # Raise an exception for bad status codes
        return response.json().get('data', {})
    except requests.exceptions.RequestException as e:
        return {'error': f'API request failed: {e}'}