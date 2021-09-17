$[cost]
=======

Directs the bot to deduct currency from the user who uses the command or optionally the targeted user.

Usage:
    $[cost ``<amount>`` ``[user]``]

Arguments:
    * ``amount`` **<required>** - Amount of currency it should cost
    * ``user`` **[optional]** - The user to deduct from the currency (if no user then it will deduct from the user issuing the command)

Example Command:
    **name**: !cost

    **response**: $[cost 50] You just paid 50 Goldfrags to use this command, ha!

    **output**::

        user:     !cost
        botisimo: You just paid 50 Goldfrags to use this command, ha!
        user:     !cost
        botisimo: Not enough Goldfrags to use that command 37/50

Example Command:
    **name**: !cost

    **response**: $[cost 50 $(1)] $(1) just lost 50 Goldfrags, ha!

    **output**::

        user:     !cost @username
        botisimo: @username just lost 50 Goldfrags, wooha!
