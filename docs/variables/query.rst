$(query)
========

Resolves the query string from the command.

Usage
    $(query ``[offset]``)

Example
    Output the query string starting with the 2nd word then the full query string::

        $(query 2) $(query)

    ``!query this is the query`` -> ``is the query this is the query``
