$(fetch)
========

Resolves the response from the url using a GET request.

.. note::

    To avoid hitting any rate limits against remote APIs, all responses are cached for 5 seconds.

Usage:
    $(fetch ``<url>``)

Arguments:
    * ``url`` **<required>** - The url to send the request to

Example Command:
    **name**: !foaas

    **response**: $(fetch https://foaas.com/you/Peter/Bob)

    **output**::

        user:     !foaas
        botisimo: Fuck you, Peter. -Bob
