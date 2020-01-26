$(rotate)
=========

Resolves a response from the given options in sequence.

Usage
    $(rotate ``<option>`` | ``[option]`` | ``[option]`` | ...)

Example
    ::

        $(rotate First response | Second response | Third response)

    ``!rotate`` -> ``First response``

    ``!rotate`` -> ``Second response``

    ``!rotate`` -> ``Third response``

    ``!rotate`` -> ``First response``
