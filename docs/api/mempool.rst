.. _mempool:

Mempool
=======

The Mempool class is available in all explorers.

Sync Usage
**********

.. code-block:: python

    from bloxplorer import bitcoin_explorer as explorer

    result = explorer.mempool.get()
    print(result.data)

Async Usage
***********

.. code-block:: python

    from bloxplorer import async_bitcoin_explorer as async_explorer

    result = await async_explorer.mempool.get()
    print(result.data)

Result
******

Both usages will output the same result data. Example output:

.. code-block:: python

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

Available methods
*****************

.. autoclass:: bloxplorer.mempool.SyncMempool
    :members:
