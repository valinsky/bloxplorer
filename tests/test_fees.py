from unittest.mock import MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.fees import SyncFees

SyncFees.make_request = MagicMock()
sync_fees = SyncFees(BITCOIN_API_BASE_URL)


def test_get_address():
    sync_fees.get_estimates()
    sync_fees.make_request.assert_called_with(http.GET, 'fee-estimates')
