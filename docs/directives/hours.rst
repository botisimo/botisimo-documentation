$[hours]
========

Directs the bot to require minimum hours for the command.

Usage
    $[hours ``<hours>``]

Example
    Send the response if the user has watched the stream for ``10`` hours::

        $[hours 10] This response will be sent only if the user has watched the stream for 10 hours

    ``!special`` -> ``This response will be sent only if the user has watched the stream for 10 hours``

    If the user has not watched the stream for long enough they will receive a direct message explaining

    ``!special`` -> ``You must watch the stream for 10 hours to unlock the !special command``
