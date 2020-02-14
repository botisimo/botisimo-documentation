$[hours]
========

Directs the bot to require minimum hours for the command.

Usage:
    $[hours ``<hours>``]

Arguments:
    * ``hours`` **<required>** - The number of hours to require the user to have

Options:
    * ``-p, --public`` **[optional]** - If present then error message will be sent to public chat (instead of direct message)
    * ``-s, --silent`` **[optional]** - If present then no error message will be sent
    * ``--error-message <message>`` **[optional]** - URL encoded error message

Example Command:
    **name**: !special

    **response**: $[hours 10] This response will be sent only if the user has watched the stream for 10 hours

    **output**::

        user:     !special
        botisimo: This response will be sent only if the user has watched the stream for 10 hours
        newbie:   !special
        botisimo: You must watch the stream for 10 hours to unlock the !special command

Example Command:
    **name**: !special

    **response**: $[hours 1 \\--error-message $(urlencode Please enjoy the show a little longer before gaining access to this command)] This response will be sent only if the user has watched the stream for 10 hours

    **output**::

        user:     !special
        botisimo: This response will be sent only if the user has watched the stream for 1 hours
        newbie:   !special
        botisimo: Please enjoy the show a little longer before gaining access to this command
