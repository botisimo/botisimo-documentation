$(fetchp)
=========

Resolves the response from the url using a POST request. Similar to :doc:`$(fetch) </variables/fetch>`.

.. note::

    To avoid hitting any rate limits against remote APIs, all responses are cached for 5 seconds.

Usage:
    $(fetchp ``<url>`` ``[data]``)

Arguments:
    * ``url`` **<required>** - The url to send the request to
    * ``data`` **[optional]** - The data string to send to the url

Example Command:
    **name**: !foaas

    **response**: $(fetchp https://foaas.com/you/Peter/Bob)

    **output**::

        user:     !foaas
        botisimo: Fuck you, Peter. -Bob
