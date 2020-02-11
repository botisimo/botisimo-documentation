!giveaway
=========

**Default Permission:** Moderator

The ``!giveaway`` command is used to create/view/close/end `giveaways <https://botisimo.com/account/giveaways>`_ via chat.

    - ``close`` - Close entry for the current giveaway `view docs`__
    - ``end`` - End a giveaway `view docs`__
    - ``new`` - Create a new giveaway `view docs`__
    - ``open`` - Open entry for the current giveaway `view docs`__
    - ``rules`` - View the rules for the current giveaway `view docs`__
    - ``view`` - View current giveaway `view docs`__
    - ``winner`` - Select a winner `view docs`__

__ #close
__ #end
__ #new
__ #open
__ #rules
__ #view
__ #winner

.. note::

    You can display the active giveaway in your stream using the `stream overlay <https://botisimo.com/account/overlays>`_ for giveaways.

close
^^^^^
Closes the giveaway to stop further entry, but keeps the results live

Usage:
    !giveaway close

Example:
    ::

        user:     !giveaway close
        botisimo: Giveaway closed: Xbox Controller Giveaway

end
^^^
Ends the giveaway

Usage:
    !giveaway end

Example:
    ::

        user:     !giveaway end
        botisimo: Giveaway ended: Xbox Controller Giveaway

new
^^^
Create a new giveaway. This will end the current giveaway if it exists.

Usage:
    !giveaway new ``<title>`` | ``[cost=0]`` | ``[multiple_entries]`` | ``[max_entries=0]`` | ``[multiple_wins]``

Arguments:
    * ``title`` **<required>** - The title of the giveaway
    * ``cost`` **[optional]** - The cost to enter the giveaway (default: 0)
    * ``multiple_entries`` **[optional]** - Set to any value to allow multiple entries (default: false)
    * ``max_entries`` **[optional]** - The maximum number of entries that a single user can enter the giveaway (0 means unlimited) (default: unlimited)
    * ``multiple_wins`` **[optional]** - Set to any value to allow a single user to win multiple times (default: false)

Example:
    ::

        user:     !giveaway new Xbox Controller Giveaway | 1500 | 1 | 0 | 1
        botisimo: New giveaway: Xbox Controller Giveaway **Type !enter to join**

open
^^^^
Opens the giveaway to allow entry

Usage:
    !giveaway open

Example:
    ::

        user:     !giveaway open
        botisimo: Giveaway opened: Xbox Controller Giveaway **Type !enter to join**

rules
^^^^^
Get the rules for the current giveaway

Usage:
    !giveaway rules

Example:
    ::

        user:     !giveaway rules
        botisimo: Giveaway rules: Must be following the channel. Must be present when doing the giveaway raffle.

view
^^^^
Get the current giveaway info

Usage:
    !giveaway

Example:
    ::

        user:     !giveaway
        botisimo: Current giveaway: Xbox Controller Giveaway **Type !enter to join**

winner
^^^^^^
Select a random winner for the giveaway

Usage:
    !giveaway winner

Example:
    ::

        user:     !giveaway winner
        botisimo: @username has won the Xbox Controller Giveaway Giveaway!
