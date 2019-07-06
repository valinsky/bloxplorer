from urllib.parse import urljoin

import requests

from blockstreamesplora.constants import BITCOIN_API_BASE_URL, LIQUID_API_BASE_URL


def get_from_path(path, **kwargs):
    url = urljoin(BITCOIN_API_BASE_URL, path)
    return _get(url, **kwargs)

def _get(url, timeout=5, headers=None, **kwargs):
    error_message = ''

    try:
        response = requests.get(url, timeout=timeout, headers=headers)
    except requests.exceptions.ConnectionError as e:
        error_message = f'Network failure: {e}'
    except requests.exceptions.Timeout as e:
        error_message = f'Request timed out: {e}'
    except requests.exceptions.RequestException as e:
        error_message = f'Request failure: {e}'
    
    if error_message:
        print(error_message)
    
    return response
