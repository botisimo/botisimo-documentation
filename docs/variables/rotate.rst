$(rotate)
=========

Resolves a response from the given options in sequence.

Usage:
    $(rotate ``<option>`` | ``[option]`` | ``[option]`` | ...)

Example Command:
    **name**: !rotate

    **response**: $(rotate First response | Second response | Third response)

    **output**::

        user:     !rotate
        botisimo: First response
        user:     !rotate
        botisimo: Second response
        user:     !rotate
        botisimo: Third response
        user:     !rotate
        botisimo: First response
