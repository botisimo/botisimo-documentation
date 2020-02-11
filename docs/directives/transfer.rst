$[transfer]
===========

Directs the bot to transfer currency from the user who uses the command to the targeted user.

Usage:
    $[transfer ``<amount>`` ``<user>``]

Arguments:
    * ``amount`` **[required]** - The amount of currency to transfer
    * ``user`` **[required]** - The user to transfer the currency to

Example Command:
    **name**: !transfer

    **response**: $[transfer 100 $(1)] You just transferred 100 Goldfrags to $(1) for using this command, woo!

    **output**::

        user:     !transfer @username
        botisimo: You just transferred 100 Goldfrags to @username for using this command, woo!
        user:     !transfer @username
        botisimo: Not enough Goldfrags to use that command 37/100
