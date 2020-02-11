$(urlencode)
============

Resolves a url encoded string.

Usage:
    $(urlencode ``<text>``)

Arguments:
    * ``text`` **<required>** - The text to url encode

Example Command:
    **name**: !encode

    **response**: $(urlencode please encode me)

    **output**::

        user:     !encode
        botisimo: please%20encode%20me
