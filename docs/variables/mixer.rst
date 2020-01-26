$(mixer)
========

Show text in Mixer chat only.

Usage
    $(mixer ``<message>``)

Example
    Output "You are a super awesome and cool dude!" when responding via Twitch chat::

        You are a $(mixer super awesome and) cool dude$(mixer !)

    ``!example`` -> mixer -> ``You are a super awesome and cool dude!``

    ``!example`` -> twitch/youtube/discord -> ``You are a cool dude``
