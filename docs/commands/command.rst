!command
========

**Default Permission:** Moderator

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

    Commands are enabled and disabled based on the platform (Twitch, Mixer, YouTube, etc.) the command was issued from. Commands will respond to the channel they are called from.

delete
^^^^^^
Delete command

Usage:
    !command delete ``<name>``

Example:
    ::

        user:     !command delete !social
        botisimo: ​Command deleted: !social

disable
^^^^^^^
Disable command

Usage:
    !command disable ``<name>``

Example:
    ::

        user:     !command disable !social
        botisimo: ​Command disabled: !social

edit
^^^^
Edit command response

Usage:
    !command edit ``<name>`` ``<response>``

Example:
    ::

        user:     !command edit !social You can follow me on twitter and instagram @botisimo
        botisimo: Command updated: !social

enable
^^^^^^
Enable command

Usage:
    !command enable ``<name>``

Example:
    ::

        user:     !command enable !social
        botisimo: Command enabled: !social

info
^^^^
Get info for a command

Usage:
    !command info ``<name>``

Example:
    ::

        user:     !command info !social
        botisimo: Command info: !social | enabled | You can follow me on twitter @botisimo

list
^^^^
List commands

Usage:
    !command list

Example:
    ::

        user:     !command list
        botisimo: Commands: !social, !wizard, !roll, !super


new
^^^
Create a new command

Usage:
    !command new ``<name>`` ``<response>``

Example:
    ::

        user:     !command new !social You can follow me on twitter @botisimo
        botisimo: New command: !social

permission
^^^^^^^^^^
Edit command minimum permission

Usage:
    !command permission ``<name>`` ``<permission=everyone|regs|subs|mods|admin>``

Example:
    ::

        user:     !command permission !social everyone
        botisimo: Command updated: !social
