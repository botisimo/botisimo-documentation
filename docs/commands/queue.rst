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

Usage
    !queue clear

Example
    Clear everyone from the queue::

        !queue clear

close
^^^^^
Close the queue

Usage
    !queue close

Example
    Close the queue::

        !queue close

join
^^^^
Join the queue

Usage
    !queue join

Example
    Join the command issuer to the queue::

        !queue join

leave
^^^^^
Leave the queue

Usage
    !queue leave

Example
    Remove the command issuer from the queue::

        !queue leave

list
^^^^
List queue

Usage
    !queue list

Example
    List users in the queue::

        !queue list

next
^^^^
Retrieve the next user(s) from the queue

Usage
    !queue next ``[users=1]``

Example
    Output the name(s) of the next user(s) in the queue and removes them from the queue. Default is ``1`` user::

        !queue next 5

open
^^^^
Open the queue

Usage
    !queue open

Example
    Open the queue::

        !queue open

permission
^^^^^^^^^^
Edit queue minimum permission

Usage
    !queue permission ``<permission=everyone|regs|subs|mods|admin>``

Example
    Edit the minimum permission for the queue to allow only ``regular`` users and above to use it::

        !queue permission regular

random
^^^^^^
Retrieve a random user from the queue as the next user

Usage
    !queue random

Example
    Output the name of the randomly selected user in the queue and removes them from the queue::

        !queue random
