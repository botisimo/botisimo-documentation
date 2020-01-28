Arguments
=========

Resolves the argument from the command input.

Usage:
    $(``<argument>`` ``[fallback]``)

Example Command:
    **name**: !example

    **response**: $(2 default text)

    **output**::

        user:     !example this is a test
        botisimo: is
        user:     !example this
        botisimo: default text
