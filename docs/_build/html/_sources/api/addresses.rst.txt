.. _addresses:

Addresses
=========

The Addresses class is available in all explorers.

Usage
*****

.. code-block:: python

    from bloxplorer import bitcoin_testnet_explorer as explorer

    result = explorer.addr.get('mwog86wxZsWf6KGufzwA69xbvzE9TGZ5vA')
    print(result.data)

    """
    {
        'address': 'mwog86wxZsWf6KGufzwA69xbvzE9TGZ5vA',
        'chain_stats': 
        {
            'funded_txo_count': 1,
            'funded_txo_sum': 4809083,
            'spent_txo_count': 0,
            'spent_txo_sum': 0,
            'tx_count': 1
        },
        'mempool_stats': 
        {
            'funded_txo_count': 0,
            'funded_txo_sum': 0,
            'spent_txo_count': 0,
            'spent_txo_sum': 0,
            'tx_count': 0
        }
    }
    """

.. autoclass:: bloxplorer.addresses.Addresses
    :members:
