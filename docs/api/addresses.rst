.. _addresses:

Addresses
=========

The Addresses class is available in all explorers.

Sync Usage
**********

.. code-block:: python

    from bloxplorer import bitcoin_explorer as explorer

    result = explorer.addr.get('bc1qgrrxw6uq7m0sxmqc4ur83v4uhwszjsrlpe9hwm')
    print(result.data)

Async Usage
***********

.. code-block:: python

    from bloxplorer import async_bitcoin_explorer as async_explorer

    result = await async_explorer.addr.get('bc1qgrrxw6uq7m0sxmqc4ur83v4uhwszjsrlpe9hwm')
    print(result.data)

Result
******

Both usages will output the same result data. Example output:

.. code-block:: python

    """
    {
        'address': 'bc1qgrrxw6uq7m0sxmqc4ur83v4uhwszjsrlpe9hwm',
        'chain_stats':
        {
            'funded_txo_count': 9,
            'funded_txo_sum': 7625024,
            'spent_txo_count': 9,
            'spent_txo_sum': 7625024,
            'tx_count': 17
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

Available methods
*****************

.. autoclass:: bloxplorer.addresses.SyncAddresses
    :members:
