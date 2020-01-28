$[give]
=======

Directs the bot to give currency to the user who uses the command or optionally the targeted user.

Usage:
    $[give ``<amount>`` ``[target]``]

Example Command:
    **name**: !give

    **response**: $[give 50] You just received 50 Goldfrags for using this command, woo!

    **output**::

        user:     !give
        botisimo: You just received 50 Goldfrags for using this command, woo!

Example Command:
    **name**: !give

    **response**: $[give 50 $(1)] $(1) just received 50 Goldfrags, woo!

    **output**::

        user:     !give @username
        botisimo: @username just received 50 Goldfrags, woo!
