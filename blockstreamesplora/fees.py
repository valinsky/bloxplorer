from blockstreamesplora.utils import Request


class Fees(Request):
    """
    Fee estimates API Wrapper
    """

    def get_fee_estimates(self):
        """
        Get an object where the key is the confirmation target (in number of blocks)
        and the value is the estimated feerate (in sat/vB).
        The available confirmation targets are 2, 3, 4, 6, 10, 20, 144, 504 and 1008 blocks.
        """
        return self.get_from_path('fee-estimates')
