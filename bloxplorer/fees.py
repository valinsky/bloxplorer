from bloxplorer.utils import Request


class Fees(Request):
    """
    Wrapper class around the Esplora Fee Estimates endpoint.

    `Blockstream Esplora Fee Estimates API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#fee-estimates>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_estimates(self, **kwargs):
        r"""
        Get an object where the key is the confirmation target (in number of blocks)
        and the value is the estimated feerate (in sat/vB).
        The available confirmation targets are 2, 3, 4, 6, 10, 20, 144, 504 and 1008 blocks.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', 'fee-estimates', **kwargs)
