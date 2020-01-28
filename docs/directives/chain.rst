$[chain]
========

Break response into multiple, chained responses.

    - `Pro members <https://botisimo.com/membership.html>`_ are limited to chaining 3 responses
    - `Master members <https://botisimo.com/membership.html>`_ are limited to chaining 5 responses
    - `Guild members <https://botisimo.com/membership.html>`_ are limited to chaining 10 responses

Usage:
    $[chain]

Example Command:
    **name**: !chain

    **response**: This is the first response $[chain] This is the second response $[chain] This is a third response

    **output**::

        user:     !chain
        botisimo: This is the first response
        botisimo: This is the second response
        botisimo: This is a third response
