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

Full documentation is available at https://valinsky.github.io/bloxplorer/

Installation
------------

To install the Bloxplorer package just run this command in your favorite terminal:

>>> pip install bloxplorer

Links
-----

* Documentation: https://valinsky.github.io/bloxplorer/
* GitHub: https://github.com/valinsky/bloxplorer
* Pypi: https://pypi.org/project/bloxplorer
* CircleCI: https://circleci.com/gh/valinsky/bloxplorer/tree/master
* License: https://github.com/valinsky/bloxplorer/blob/master/LICENSE

Tips
----

You already know :) 

฿itcoin address: **3NRWkeb9HtQn6sGHNyAXhkcoCcUwstpdBb**

Thank you!!

.. |circle| image:: https://circleci.com/gh/valinsky/bloxplorer/tree/master.svg?style=shield
    :target: https://circleci.com/gh/valinsky/bloxplorer/tree/master

.. |version| image:: https://img.shields.io/badge/version-0.1.1-blue
    :target: https://pypi.org/project/bloxplorer/

.. |MIT license| image:: https://img.shields.io/badge/license-MIT-orange
    :target:  https://github.com/valinsky/bloxplorer/blob/master/LICENSE
