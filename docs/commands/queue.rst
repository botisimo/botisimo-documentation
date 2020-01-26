!queue
======
The ``!queue`` command is used to join/leave/list users in the queue via chat

    - ``clear`` - Clear the queue `view docs <#clear>`_
    - ``close`` - Close the queue `view docs <#close>`_
    - ``join`` - Join the queue `view docs <#join>`_
    - ``leave`` - Leave the queue `view docs <#leave>`_
    - ``list`` - List users in queue `view docs <#list>`_
    - ``next`` - Get the next user in the queue `view docs <#next>`_
    - ``open`` - Open the queue `view docs <#open>`_
    - ``permission`` - Edit queue minimum permission `view docs <#permission>`_
    - ``random`` - Gets a random user in the queue as the next user `view docs <#random>`_

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
