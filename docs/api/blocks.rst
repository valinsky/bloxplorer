.. _blocks:

Blocks
======

The Blocks class is available in all explorers.

Usage
*****

.. code-block:: python

    from bloxplorer import bitcoin_testnet_explorer as explorer

    result = explorer.blocks.get('00000000000001bcfbd6242711752c6d8eb15701eb19e410a39a45fa363926e9')
    print(result.data)

    """
    {
        'id': '00000000000001bcfbd6242711752c6d8eb15701eb19e410a39a45fa363926e9',
        'height': 1572304,
        'version': 536870912,
        'timestamp': 1564789315,
        'tx_count': 71,
        'size': 22381,
        'weight': 71122,
        'merkle_root': '55cdb5be1689027c81c9bf8731c05f955be49eece5639d99ad95ccbf9374cada',
        'previousblockhash': '00000000000001decd01ced9b0b98f15ffb600f6abd27e0634809a90268b3765',
        'nonce': 2812464956,
        'bits': 436412916
    }
    """

.. autoclass:: bloxplorer.blocks.Blocks
    :members:
