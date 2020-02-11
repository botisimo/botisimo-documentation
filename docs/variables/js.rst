$(js)
=====

Resolves the value of a javascript expression

Usage:
    $(js ``<javascript>``)

Arguments:
    * ``javascript`` **<required>** - The javascript expression to evaluate

Example Command:
    **name**: !js

    **response**: $(js ['need', 'a', 'better', 'example'].join(' '))

    **output**::

        user:     !js
        botisimo: need a better example
