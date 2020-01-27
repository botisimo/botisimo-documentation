!command
========

The ``!command`` command is used to create/edit/delete/enable/disable `custom commands <https://botisimo.com/account/commands>`_ via chat.

    - ``delete`` - Delete command `view docs`__
    - ``disable`` - Disable command `view docs`__
    - ``edit`` - Edit command response `view docs`__
    - ``enable`` - Enable command `view docs`__
    - ``info`` - View command info `view docs`__
    - ``list`` - List commands `view docs`__
    - ``new`` - Create a new command `view docs`__
    - ``permission`` - Edit command minimum permission `view docs`__

__ #delete
__ #disable
__ #edit
__ #enable
__ #info
__ #list
__ #new
__ #permission

.. note::

    If a command argument is required it will be wrapped in ``<`` ``>`` and if the argument is optional it will be wrapped in ``[`` ``]``.

.. note::

    Commands are enabled and disabled based on the platform (Twitch, Mixer, YouTube, etc.) the command was issued from. Commands will respond to the channel they are called from.

delete
^^^^^^
Delete command

Usage
    !command delete ``<name>``

Example
    Delete the command named ``!social``::

        !command delete !social

disable
^^^^^^^
Disable command

Usage
    !command disable ``<name>``

Example
    Disable the command named ``social`` but does not delete it::

        !command disable !social

edit
^^^^
Edit command response

Usage
    !command edit ``<name>`` ``<response>``

Example
    Edit the command named ``!social`` to respond with ``You can follow me on twitter and instagram @botisimo``::

        !command edit !social You can follow me on twitter and instagram @botisimo

enable
^^^^^^
Enable command

Usage
    !command enable ``<name>``

Example
    Enable the command named ``social``::

        !command enable !social

info
^^^^
Get info for a command

Usage
    !command info ``<name>``

Example
    Output the details for the ``!social`` command::

        !command info !social

list
^^^^
List commands

Usage
    !command list

Example
    List commands available in Botisimo::

        !command list

new
^^^
Create a new command

Usage
    !command new ``<name>`` ``<response>``

Example
    Create a new command named ``!social`` that responds with ``You can follow me on twitter @botisimo``::

        !command new !social You can follow me on twitter @botisimo

permission
^^^^^^^^^^
Edit command minimum permission

Usage
    !command permission ``<name>`` ``<permission=everyone|regs|subs|mods|admin>``

Example
    Edit the minimum permission for the command named ``!social`` to allow ``everyone`` to use it::

        !command permission !social everyone
