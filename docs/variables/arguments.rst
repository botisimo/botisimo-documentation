Arguments
=========

Resolves the argument from the command input.

Usage
    $(``<argument>`` ``[fallback]``)

Example
    Output the 2nd argument after the command and optionally uses the ``fallback`` text if no argument found::

        $(2 default text)

    ``!example this is a test`` -> ``is``

    ``!example this`` -> ``default text``
