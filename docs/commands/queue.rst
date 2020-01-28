!queue
======
The ``!queue`` command is used to join/leave/list users in the queue via chat

    - ``clear`` - Clear the queue `view docs`__
    - ``close`` - Close the queue `view docs`__
    - ``join`` - Join the queue `view docs`__
    - ``leave`` - Leave the queue `view docs`__
    - ``list`` - List users in queue `view docs`__
    - ``next`` - Get the next user in the queue `view docs`__
    - ``open`` - Open the queue `view docs`__
    - ``permission`` - Edit queue minimum permission `view docs`__
    - ``random`` - Gets a random user in the queue as the next user `view docs`__

__ #clear
__ #close
__ #join
__ #leave
__ #list
__ #next
__ #open
__ #permission
__ #random

clear
^^^^^
Clear the queue

Usage:
    !queue clear

Example:
    ::

        user:     !queue clear
        botisimo: Queue cleared

close
^^^^^
Close the queue

Usage:
    !queue close

Example:
    ::

        user:     !queue close
        botisimo: ​Queue closed

join
^^^^
Join the queue

Usage:
    !queue join

Example:
    ::

        user:     !queue join
        botisimo: Added to queue: @user

leave
^^^^^
Leave the queue

Usage:
    !queue leave

Example:
    ::

        user:     !queue leave
        botisimo: ​Removed from queue: @user

list
^^^^
List queue

Usage:
    !queue list

Example:
    ::

        user:     !queue list
        botisimo: Queue: @user

next
^^^^
Retrieve the next user(s) from the queue

Usage:
    !queue next ``[users=1]``

Example:
    ::

        user:     !queue next
        botisimo: Next in queue: @user

open
^^^^
Open the queue

Usage:
    !queue open

Example:
    ::

        user:     !queue open
        botisimo: ​Queue opened

permission
^^^^^^^^^^
Edit queue minimum permission

Usage:
    !queue permission ``<permission=everyone|regs|subs|mods|admin>``

Example:
    ::

        user:     !queue permission everyone
        botisimo: Queue permission updated: everyone


random
^^^^^^
Retrieve a random user from the queue as the next user

Usage:
    !queue random

Example:
    ::

        user:     !queue random
        botisimo: ​Next in queue: @user
