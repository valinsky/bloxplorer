Bloxplorer
==========

|circle| |version| |MIT license|

**Bloxplorer** is a simple yet very effective Bitcoin and Liquid blockchain explorer.

It allows developers to make use of the full power of the `Blockstream Esplora HTTP API 
<https://github.com/Blockstream/esplora>`_ through a clean Python interface.

Usage
-----

Using the Bloxplorer package is easy and straightforward, as it should be.

.. code-block:: python

    from bloxplorer import bitcoin_explorer

    response = bitcoin_explorer.blocks.get_last_height()
    print(response.data)
    '586438'

Installation
------------

To install the Bloxplorer package just run this command in your favorite terminal:

>>> pip install bloxplorer

Documentation
-------------

Full documentation is avaliable at http://docs.python-bloxplorer.org/.

Tips
----

Tips: `3NRWkeb9HtQn6sGHNyAXhkcoCcUwstpdBb`

.. |circle| image:: https://circleci.com/gh/valinsky/bloxplorer/tree/master.svg?style=svg
    :target: https://circleci.com/gh/valinsky/bloxplorer/tree/master

.. |version| image:: https://img.shields.io/pypi/v/nine?logo=bloxplorer
    :target: https://pypi.org/project/bloxplorer/

.. |MIT license| image:: https://img.shields.io/badge/license-MIT-orange
    :target: https://pypi.org/project/bloxplorer/
