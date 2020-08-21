$(discord)
==========

Show text in Discord chat only.

Usage:
    $(discord ``<message>``)

Arguments:
    * ``message`` **<required>** - The message to display in chat

Example Command:
    **name**: !example

    **response**: You are a $(discord super awesome and) cool dude$(discord !)

    **discord output**::

        user:     !example
        botisimo: You are a super awesome and cool dude!

    **twitch/youtube output**::

        user:     !example
        botisimo: You are a cool dude
