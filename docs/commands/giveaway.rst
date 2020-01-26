!giveaway
=========

The ``!giveaway`` command is used to create/view/close/end `giveaways <https://botisimo.com/account/giveaways>`_ via chat.

    - ``close`` - Close entry for the current giveaway `view docs <#close>`_
    - ``end`` - End a giveaway `view docs <#end>`_
    - ``new`` - Create a new giveaway `view docs <#new>`_
    - ``open`` - Open entry for the current giveaway `view docs <#open>`_
    - ``rules`` - View the rules for the current giveaway `view docs <#rules>`_
    - ``view`` - View current giveaway `view docs <#view>`_
    - ``winner`` - Select a winner `view docs <#winner>`_

.. note::

    If a command argument is required it will be wrapped in ``<`` ``>`` and if the argument is optional it will be wrapped in ``[`` ``]``.

.. note::

    You can display the active giveaway in your stream using the `stream overlay <https://botisimo.com/account/overlays>`_ for giveaways.

close
^^^^^
Closes the giveaway to stop further entry, but keeps the results live

Usage
    !giveaway close

Example
    ::

        !giveaway close

end
^^^
Ends the giveaway

Usage
    !giveaway end

Example
    ::

        !giveaway end

new
^^^
Create a new giveaway. This will end the current giveaway if it exists.

Usage
    !giveaway new ``<title>`` | ``[cost=0]`` | ``[multiple_entries]`` | ``[max_entries=0]`` | ``[multiple_wins]``

Example
    Create a new giveaway with the title ``Xbox Controller Giveaway`` that costs ``1500`` currency to enter. This giveaway allows unlimited entries per user and allows them to win multiple times::

        !giveaway new Xbox Controller Giveaway | 1500 | 1 | 0 | 1

open
^^^^
Opens the giveaway to allow entry

Usage
    !giveaway open

Example
    ::

        !giveaway open

rules
^^^^^
Get the rules for the current giveaway

Usage
    !giveaway rules

Example
    Output the current giveaway rules to the chat. If there is no giveaway or no rules then there is no response::

        !giveaway rules


view
^^^^
Get the current giveaway info

Usage
    !giveaway

Example
    Outputs the current giveaway to the chat. If there is no giveaway then there is no response::

        !giveaway

winner
^^^^^^
Select a random winner for the giveaway

Usage
    !giveaway winner

Example
    Selects a random winner for the giveaway::

        !giveaway winner
