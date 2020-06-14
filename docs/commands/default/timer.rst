!timer
======

**Default Permission:** Moderator

The ``!timer`` command is used to create/edit/delete/start/stop `custom timers <https://botisimo.com/account/timers>`_ via chat.

    - ``delete`` - Delete a timer `view docs`__
    - ``edit`` - Edit a timer `view docs`__
    - ``info`` - View timer info `view docs`__
    - ``list`` - List timers `view docs`__
    - ``new`` - Create a new timer `view docs`__
    - ``start`` - Start a timer `view docs`__
    - ``stop`` - Stop a timer `view docs`__

__ #delete
__ #edit
__ #info
__ #list
__ #new
__ #start
__ #stop

.. note::

    Timers are started and stopped based on the platform (Twitch, Mixer, YouTube, etc.) the command was issued from. Timers will only post to a single channel per platform.

.. note::

    Timers are only activated if 10 or more messages have been sent since the last time it was activated.

delete
^^^^^^
Delete a timer

Usage:
    !timer delete ``<name>``

Arguments:
    * ``name`` **<required>** - The name of the timer to delete

Example:
    ::

        user:     !timer delete social
        botisimo: ​​Timer deleted: social

edit
^^^^
Edit a timer

Usage:
    !timer edit ``<name>`` ``<interval>`` ``<message>``

Arguments:
    * ``name`` **<required>** - The name of the timer
    * ``interval`` **<required>** - The interval of the timer in minutes (valid values: ``5`` to ``60``)
    * ``message`` **<required>** - The message for the timer

Example:
    ::

        user:     !timer edit social 10 Follow me on twitter and instagram @botisimo
        botisimo: Timer updated: social

info
^^^^
Get info for a timer

Usage:
    !timer info ``<name>``

Arguments:
    * ``name`` **<required>** - The name of the timer to get the info for

Example:
    ::

        user:     !timer info social
        botisimo: Timer info: social | 5m | started | Follow me on twitter @botisimo

list
^^^^
List timers

Usage:
    !timer list

Example:
    ::

        user:     !timer list
        botisimo: ​Timers: social, follow, botisimo

new
^^^
Create a new timer

Usage:
    !timer new ``<name>`` ``<interval>`` ``<message>``

Arguments:
    * ``name`` **<required>** - The name of the timer
    * ``interval`` **<required>** - The interval of the timer in minutes (valid values: ``5`` to ``60``)
    * ``message`` **<required>** - The message for the timer

Example:
    ::

        user:     !timer new social 5 Follow me on twitter @botisimo
        botisimo: ​New timer: social

start
^^^^^
Starts a timer in the current channel

Usage:
    !timer start ``<name>``

Arguments:
    * ``name`` **<required>** - The name of the timer to start

Example:
    ::

        user:     !timer start social
        botisimo: ​Timer started: social

stop
^^^^
Stops a timer

Usage:
    !timer stop ``<name>``

Arguments:
    * ``name`` **<required>** - The name of the timer to stop

Example:
    ::

        user:     !timer stop social
        botisimo: ​Timer stopped: social
