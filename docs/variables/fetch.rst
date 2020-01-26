$(fetch)
========

Resolves the response from the url using a GET request.

.. note::

    Responses are cached for 5 seconds.

Usage
    $(fetch ``<url>``)

Example
    ::

        $(fetch https://foaas.com/you/Peter/Bob)

    ``!foaas`` -> ``Fuck you, Peter. -Bob``
