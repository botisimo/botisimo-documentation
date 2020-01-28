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

    You can display the active poll in your stream using the `stream overlay <https://botisimo.com/account/overlays>`_ for polls.

close
^^^^^
Closes the poll to stop further voting, but keeps the results live

Usage:
    !poll close

Example:
    ::

        user:     !poll close
        botisimo: ​Poll voting closed

end
^^^
Ends the poll

Usage:
    !poll end

Example:
    ::

        user:     !poll end
        botisimo: ​poll ended

new
^^^
Create a new poll. This will end the current poll if it exists.

Usage:
    !poll new ``<option>`` | ``[option]`` | ``[option]`` | ...

Example:
    ::

        user:     !poll new Is this a fun poll? | yes | no | hell no | what a stupid poll
        botisimo: New poll: Is this a fun poll? 1. yes (0 votes) 2. no (0 votes) 3. hell no (0 votes) 4. what a stupid poll (0 votes)

open
^^^^
Opens the poll to allow voting

Usage:
    !poll open

Example:
    ::

        user:     !poll open
        botisimo: Poll voting opened: Is this a fun poll? 1. yes (0 votes) 2. no (0 votes) 3. hell no (0 votes) 4. what a stupid poll (0 votes)

view
^^^^
Get the current poll info

Usage:
    !poll

Example:
    ::

        user:     !poll
        botisimo: ​​Current poll: Is this a fun poll? 1. yes (0 votes) 2. no (0 votes) 3. hell no (0 votes) 4. what a stupid poll (0 votes)

winner
^^^^^^
Select a random winner from the given option

Usage:
    !poll winner ``<option>``

Example:
    ::

        user:     !poll winner 1
        botisimo: ​#1 yes wins!
