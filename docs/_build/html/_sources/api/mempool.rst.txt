.. _mempool:

Mempool
=======

The Mempool class is available in all explorers.

Usage
*****

.. code-block:: python

    from bloxplorer import bitcoin_testnet_explorer as explorer

    result = explorer.mempool.get()
    print(result.data)

    """
    {
        'count': 8,
        'vsize': 2023,
        'total_fee': 7069,
        'fee_histogram': [
            [
                1.0,
                2023
            ]
        ]
    }
    """

.. autoclass:: bloxplorer.mempool.Mempool
    :members:
