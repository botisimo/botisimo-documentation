$[cost]
=======

Directs the bot to add a currency cost to the command.

Usage:
    $[cost ``<amount>``]

Arguments:
    * ``amount`` **<required>** - Amount of currency it should cost

Example Command:
    **name**: !cost

    **response**: $[cost 50] You just paid 50 Goldfrags to use this command, ha!

    **output**::

        user:     !cost
        botisimo: You just paid 50 Goldfrags to use this command, ha!
        user:     !cost
        botisimo: Not enough Goldfrags to use that command 37/50
