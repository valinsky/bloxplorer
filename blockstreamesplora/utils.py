from urllib.parse import urljoin

import requests

from blockstreamesplora.constants import BITCOIN_API_BASE_URL, DEFAULT_TIMEOUT
from blockstreamesplora.exceptions import BlockstreamExplorerError


class Request:

    BASE_API_URL = BITCOIN_API_BASE_URL

    def get_from_path(self, path, **kwargs):
        url = urljoin(self.BASE_API_URL, path)
        return self._get(url, **kwargs)

    @staticmethod
    def _get(url, timeout=DEFAULT_TIMEOUT, headers=None, **kwargs):
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
        except requests.exceptions.RequestException:
            raise
        return response
