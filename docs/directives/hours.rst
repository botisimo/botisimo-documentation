$[hours]
========

Directs the bot to require minimum hours for the command.

Usage:
    $[hours ``<hours>``]

Arguments:
    * ``hours`` **[required]** - The number of hours to require the user to have

Example Command:
    **name**: !special

    **response**: $[hours 10] This response will be sent only if the user has watched the stream for 10 hours

    **output**::

        user:     !special
        botisimo: This response will be sent only if the user has watched the stream for 10 hours
        newbie:   !special
        botisimo: You must watch the stream for 10 hours to unlock the !special command
