$[cooldown]
===========

Directs the bot to enforce a cooldown in seconds for the command.

Usage:
    $[cooldown ``<seconds>``]

Arguments:
    * ``seconds`` **<required>** - Number of seconds it should wait to cooldown

Options:
    * ``-p, --public`` **[optional]** - If present then error message will be sent to public chat (instead of direct message)
    * ``-s, --silent`` **[optional]** - If present then no error message will be sent
    * ``-g, --global`` **[optional]** - If present then cooldown will apply to any user who tries to use the command
    * ``--error-message <message>`` **[optional]** - URL encoded error message

Example Command:
    **name**: !cool

    **response**: $[cooldown 30 \\--public] This response will be sent only if 30 seconds has passed

    **output**::

        user:     !cool
        botisimo: This response will be sent only if 30 seconds has passed
        user:     !cool
        botisimo: You must wait 30 seconds between !cool commands

Example Command:
    **name**: !cool

    **response**: $[cooldown 30 \\--silent] This response will be sent only if 30 seconds has passed

    **output**::

        user:     !cool
        botisimo: This response will be sent only if 30 seconds has passed
        user:     !cool

Example Command:
    **name**: !cool

    **response**: $[cooldown 30 \\--error-message $(urlencode Cool it dude, you gotta wait 30 seconds to use this command again)] This response will be sent only if 30 seconds has passed

    **output**::

        user:     !cool
        botisimo: This response will be sent only if 30 seconds has passed
        user:     !cool
        botisimo: Cool it dude, you gotta wait 30 seconds to use this command again
