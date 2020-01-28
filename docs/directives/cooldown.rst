$[cooldown]
===========

Directs the bot to enforce a cooldown in seconds for the command.

Usage:
    $[cooldown ``<seconds>``]

Example Command:
    **name**: !cool

    **response**: $[cooldown 30] This response will be sent only if 30 seconds has passed

    **output**::

        user:     !cool
        botisimo: This response will be sent only if 30 seconds has passed
        user:     !cool
        botisimo: You must wait 30 seconds between !cool commands
