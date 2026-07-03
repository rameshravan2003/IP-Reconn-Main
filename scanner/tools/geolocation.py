import requests

def get_geolocation(ip_address):
    """
    Gets geolocation data from the API.
    """
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}', timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': f'A network error occurred: {e}'}