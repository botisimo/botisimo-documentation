$(twitch)
=========

Show text in Twitch chat only.

Usage:
    $(twitch ``<message>``)

Arguments:
    * ``message`` **<required>** - The message to display in chat

Example Command:
    **name**: !example

    **response**: You are a $(twitch super awesome and) cool dude$(twitch !)

    **twitch output**::

        user:     !example
        botisimo: You are a super awesome and cool dude!

    **youtube/discord output**::

        user:     !example
        botisimo: You are a cool dude
