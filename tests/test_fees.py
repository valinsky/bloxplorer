from unittest.mock import MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL
from bloxplorer.fees import Fees


Fees.make_request = MagicMock()
fees = Fees(BITCOIN_API_BASE_URL)


def test_get_address():
    fees.get_estimates()
    fees.make_request.assert_called_with('GET', 'fee-estimates')
