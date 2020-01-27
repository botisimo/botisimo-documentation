!poll
=====

The ``!poll`` command is used to create/view/close/end `polls <https://botisimo.com/account/polls>`_ via chat.

    - ``close`` - Close voting for a poll `view docs`__
    - ``end`` - End a poll `view docs`__
    - ``new`` - Create a new poll `view docs`__
    - ``open`` - Open voting for a poll `view docs`__
    - ``view`` - View current poll `view docs`__
    - ``winner`` - Select a winner `view docs`__

__ #close
__ #end
__ #new
__ #open
__ #view
__ #winner

.. note::

    If a command argument is required it will be wrapped in ``<`` ``>`` and if the argument is optional it will be wrapped in ``[`` ``]``.

.. note::

    You can display the active poll in your stream using the `stream overlay <https://botisimo.com/account/overlays>`_ for polls.

close
^^^^^
Closes the poll to stop further voting, but keeps the results live

Usage
    !poll close

Example
    ::

        !poll close

end
^^^
Ends the poll

Usage
    !poll end

Example
    ::

        !poll end

new
^^^
Create a new poll. This will end the current poll if it exists.

Usage
    !poll new ``<option>`` | ``[option]`` | ``[option]`` | ...

Example
    Creates a new poll with the options ``yes``, ``no``, ``hell no``, and ``what a stupid poll``::

        !poll new Is this a fun poll? | yes | no | hell no | what a stupid poll

open
^^^^
Opens the poll to allow voting

Usage
    !poll open

Example
    ::

        !poll open

view
^^^^
Get the current poll info

Usage
    !poll

Example
    Outputs the current poll and standings to the chat. If there is no poll there is no response::

        !poll

winner
^^^^^^
Select a random winner from the given option

Usage
    !poll winner ``<option>``

Example
    Sets the winning option to option ``1`` and rewards and users who voted on that option with currency based on their bet::

        !poll winner 1
