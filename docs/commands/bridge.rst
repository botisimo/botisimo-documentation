!bridge (Discord only)
======================

A Discord bridge is a way to send messages between multiple Discord servers running Botisimo. The `!bridge` command is used to create/join/leave/delete Discord bridges via chat.

    - ``delete`` - Delete or leave a bridge `view docs`__
    - ``join`` - Join a bridge `view docs`__
    - ``new`` - Create a new bridge to host `view docs`__

__ #delete
__ #join
__ #new

delete
^^^^^^
Delete a bridge

Usage
    !bridge delete

Example
    Delete the entire bridge if you are the host. Disconnect from the bridge if you are not the host::

        !bridge delete

    ``!bridge delete`` -> ``Bridge deleted``

join
^^^^
Join a bridge using a token

Usage
    !bridge ``<token>``

Example
    Join the bridge with token ``ggh4jd7f``::

        !bridge ggh4jd7f

    ``!bridge ggh4jd7f`` -> ``You have been connected to the bridge``

new
^^^
Create a new bridge

Usage
    !bridge

Example
    Create a new bridge and get a token for other channels to join the bridge::

        !bridge

    ``!bridge`` -> ``This channel is now hosting a bridge. Add other channels to this bridge by typing '!bridge ggh4jd7f' in those channels.``
