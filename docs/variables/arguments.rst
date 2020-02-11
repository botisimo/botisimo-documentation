Arguments
=========

Resolves the argument from the command input.

Usage:
    $(``<argument>`` ``[fallback]``)

Arguments:
    ``argument`` **<required>** - The number of the argument to get from the command starting with 1
    ``fallback`` **[optional]** - The text to display if the argument does not exist

Example Command:
    **name**: !hello

    **response**: Hello $(1 World)!

    **output**::

        user:     !hello @username
        botisimo: Hello @username!
        user:     !hello
        botisimo: Hello World!
