.. _fee_estimates:

Fee Estimates
=============

The Fee Estimates class is available in all explorers.

Sync Usage
**********

.. code-block:: python

    from bloxplorer import bitcoin_explorer as explorer

    result = explorer.fees.get_estimates()
    print(result.data)

Async Usage
***********

.. code-block:: python

    from bloxplorer import async_bitcoin_explorer as async_explorer

    result = await async_explorer.fees.get_estimates()
    print(result.data)

Result
******

Both usages will output the same result data. Example output:

.. code-block:: python

    """
    {
        '25': 1.014,
        '144': 0.8739999999999999,
        '504': 0.8739999999999999,
        '10': 1.014,
        '3': 1.08,
        '17': 1.014,
        '23': 1.014
    }
    """

Available methods
*****************

.. autoclass:: bloxplorer.fees.SyncFees
    :members:
