$(cache)
========

Resolve a value from the cache. Values can be save to the cache using the :doc:`cache directive </directives/cache>`.

Usage
    $(cache ``<key>``)

Example
    Output the value in the cache for the username, if any::

        You have a cached value of "$(cache $(username))"

    ``!cache`` -> ``You have a cached value of "some value to save for later"``
