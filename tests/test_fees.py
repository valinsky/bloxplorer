from unittest.mock import MagicMock

from blockstreamesplora.fees import Fees


Fees.get_from_path = MagicMock()
fees = Fees()


def test_get_address():
    fees.get_fee_estimates()
    fees.get_from_path.assert_called_with('fee-estimates')
