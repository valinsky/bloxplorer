.. _fee_estimates:

Fee Estimates
=============

The Fee Estimates class is available in all explorers.

Usage
*****

.. code-block:: python

    from bloxplorer import bitcoin_testnet_explorer as explorer

    result = explorer.fees.get_estimates()
    print(result.data)

    """
    {
        '2': 1,
        '3': 1,
        '4': 1,
        '6': 1,
        '10': 1,
        '20': 1,
        '144': 1,
        '504': 1,
        '1008': 1
    }
    """

.. autoclass:: bloxplorer.fees.Fees
    :members:
