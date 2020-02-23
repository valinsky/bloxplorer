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

Timeouts
********

You can tell Bloxplorer to stop waiting for a response from the Blockstream API after 
a given number of seconds with the **timeout** parameter. 
By default the timeout is set to 5 seconds.

    >>> bitcoin_explorer.blocks.get_blocks(start_height='587840', timeout=3)

Exceptions
**********

There are 2 different types of exceptions that can be raised, client and API exceptions.

**Client Exceptions**

In the event of a network problem (e.g. DNS failure, refused connection, etc), 
BlockstreamClientNetworkError will be raised.

In the event of a Timeout, BlockstreamClientTimeout will be raised.

For anything else, Bloxplorer will raise a BlockstreamClientError.

These exceptions will be accompanied by the error message, the resource url and the http method.

**API Exceptions**

In the event of an API error (e.g. Invalid resource, Bad Request, etc), Bloxplorer will
raise BlockstreamApiError.

This exception will provide the same data as the Client exceptions, alongside the status code.

Source Code
***********

Bloxplorer is available on GitHub -> `right here <https://github.com/valinsky/bloxplorer>`_.

Clone the public repository:

    >>> git clone https://github.com/valinsky/bloxplorer.git

Dependencies
************

Bloxplorer uses the beautiful `Requests <https://github.com/requests/requests>`_ package for 
its HTTP calls. Big shout out to the `Requests <https://github.com/requests/requests>`_ team.
