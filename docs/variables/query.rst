$(query)
========

Resolves the query string from the command.

Usage:
    $(query ``[start]``)

Arguments:
    * ``start`` **[optional]** - The word to start on from the beginning of the query

Example Command:
    **name**: !query

    **response**: $(query) -> $(query 3)

    **output**::

        user:     !query this is the query
        botisimo: this is the query -> the query
