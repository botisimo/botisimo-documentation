$(cache)
========

Resolve a value from the cache. Values can be save to the cache using the :doc:`cache directive </directives/cache>`.

Usage:
    $(cache ``<key>``)

Example Command:
    **name**: !cache

    **response**: You have a cached value of "$(cache $(username))"

    **output**::

        user:     !cache
        botisimo: You have a cached value of "some value to save for later"
