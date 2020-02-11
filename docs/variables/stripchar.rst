$(stripchar)
============

Strip a character from text.

Usage:
    $(stripchar ``<character>`` ``<text>``)

Arguments:
    * ``character`` **<required>** - The character to remove from the text
    * ``text`` **<required>** - The text to remove the character from

Example Command:
    **name**: !shoutout

    **response**: $(1) is one cool streamer, check them out at https://mixer.com/$(stripchar @ $(1))

    **output**::

        user:     !shoutout @username
        botisimo: @username is one cool streamer, check them out at https://mixer.com/username
