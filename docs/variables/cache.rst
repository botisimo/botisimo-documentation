$(cache)
========

Resolve a value from the cache. Values can be saved to the cache using the :doc:`cache directive </directives/cache>`.

Usage:
    $(cache ``<key>``)

Arguments:
    ``key`` **<required>** - The key of the value to fetch from the cache

Example Command:
    **name**: !cache

    **response**: You have a cached value of "$(cache $(username))"

    **output**::

        user:     !cache
        botisimo: You have a cached value of "some value to save for later"
