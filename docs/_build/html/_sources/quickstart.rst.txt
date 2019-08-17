.. _quickstart:

Quickstart
==========

Using the Bloxplorer package is easy and straightforward, as it should be.

Setup
*****

To install the Bloxplorer package just run this command in your favorite terminal:

    >>> pip install bloxplorer

Usage
*****

After installation you may import and use the desired explorer and all 
of its associated methods. The available explorers are Bitcoin, Liquid and Bitcoin Testnet:

Bitcoin Explorer
----------------

.. code-block:: python

    from bloxplorer import bitcoin_explorer

    result = bitcoin_explorer.blocks.get_last_height()
    print(result.data)
    '587840'

Liquid Explorer
---------------

.. code-block:: python

    from bloxplorer import liquid_explorer

    result = liquid_explorer.blocks.get_last_height()
    print(result.data)
    '412287'

Bitcoin Testnet Explorer
------------------------

.. code-block:: python

    from bloxplorer import bitcoin_testnet_explorer

    result = bitcoin_testnet_explorer.blocks.get_last_height()
    print(result.data)
    '1571699'

For a full list of available API methods :ref:`click here <api>`.

Source Code
***********

Bloxplorer is available on GitHub -> `right here <https://github.com/valinsky/bloxplorer>`_.

Clone the public repository:

    >>> git clone https://github.com/valinsky/bloxplorer.git

Dependencies
************

Bloxplorer uses the beautiful `Requests <https://github.com/requests/requests>`_ package for 
its HTTP calls. Big shout out to the `Requests <https://github.com/requests/requests>`_ team.
