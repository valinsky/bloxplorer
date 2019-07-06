from urllib.parse import urljoin

import requests

from blockstreamesplora.constants import BITCOIN_API_BASE_URL


class Request:

    BASE_API_URL = BITCOIN_API_BASE_URL

    def get_from_path(self, path, **kwargs):
        url = urljoin(self.BASE_API_URL, path)
        return self._get(url, **kwargs)

    @staticmethod
    def _get(url, timeout=5, headers=None, **kwargs):
        error_message = ''

        try:
            response = requests.get(url, timeout=timeout, headers=headers)
        except requests.exceptions.ConnectionError as e:
            # raise
            error_message = f'Network failure: {e}'
        except requests.exceptions.Timeout as e:
            # raise
            error_message = f'Request timed out: {e}'
        except requests.exceptions.RequestException as e:
            # raise
            error_message = f'Request failure: {e}'
        
        if error_message:
            print(error_message)
        
        return response
