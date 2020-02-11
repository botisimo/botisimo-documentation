$[cache]
========

Saves a value temporarily to be used in other commands. Fetch values from the cache using the :doc:`cache variable </variables/cache>`. The cache is not meant to be used as a long term or permanent place to store any sensitive or important information.

Usage:
    $[cache ``<key>`` ``<seconds>`` ``<value>``]

Arguments:
    * ``key`` **<required>** - The key to store the value in the cache
    * ``seconds`` **<required>** - Number of seconds to keep the value in the cache
    * ``value`` **<required>** - The value to store in the cache

Example Command:
    **name**: !cache

    **response**: $[cache $(username) 60 some value to save for later] value saved

    **output**::

        user:     !cache
        botisimo: value saved
