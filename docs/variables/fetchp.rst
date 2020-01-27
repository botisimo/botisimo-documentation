$(fetchp)
=========

Resolves the response from the url using a POST request. Similar to :doc:`$(fetch) </variables/fetch>`.

.. note::

    Responses are cached for 5 seconds.

Usage
    $(fetchp ``<url>`` ``[data]``)

Example
    ::

        $(fetchp https://foaas.com/you/Peter/Bob)

    ``!foaas`` -> ``Fuck you, Peter. -Bob``
