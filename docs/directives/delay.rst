$[delay]
========

Directs the bot to wait some seconds before responding.

Usage:
    $[delay ``<seconds>``]

Arguments:
    * ``seconds`` **<required>** - The number of seconds it should delay

Example Command:
    **name**: !delay

    **response**: $[delay 5] This response will be sent after 5 seconds

    **output**::

        user:     !delay

        ... wait 5 seconds ...

        botisimo: This response will be sent after 5 seconds
