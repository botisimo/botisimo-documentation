$(twitch)
=========

Show text in Twitch chat only.

Usage
    $(twitch ``<message>``)

Example
    Output "You are a super awesome and cool dude!" when responding via Twitch chat::

        You are a $(twitch super awesome and) cool dude$(twitch !)

    ``!example`` -> twitch -> ``You are a super awesome and cool dude!``

    ``!example`` -> mixer/youtube/discord -> ``You are a cool dude``
