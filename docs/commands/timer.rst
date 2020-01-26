!timer
======

The ``!timer`` command is used to create/edit/delete/start/stop `custom timers <https://botisimo.com/account/timers>`_ via chat.

    - ``delete`` - Delete a timer `view docs <#delete>`_
    - ``edit`` - Edit a timer `view docs <#edit>`_
    - ``info`` - View timer info `view docs <#info>`_
    - ``list`` - List timers `view docs <#list>`_
    - ``new`` - Create a new timer `view docs <#new>`_
    - ``start`` - Start a timer `view docs <#start>`_
    - ``stop`` - Stop a timer `view docs <#stop>`_

.. note::

    If a command argument is required it will be wrapped in ``<`` ``>`` and if the argument is optional it will be wrapped in ``[`` ``]``.

.. note::

    Timers are started and stopped based on the platform (Twitch, Mixer, YouTube, etc.) the command was issued from. Timers will only post to a single channel per platform.

.. note::

    Timers are only activated if 10 or more messages have been sent since the last time it was activated.

delete
^^^^^^
Delete a timer

Usage
    !timer delete ``<name>``

Example
    Delete the timer named ``social``::

        !timer delete social

edit
^^^^
Edit a timer

Usage
    !timer edit ``<name>`` ``<interval>`` ``<message>``

Example
    Edit the timer named ``social`` to post the message every 10 minutes in the current channel::

        !timer edit social 10 Follow me on twitter and instagram @botisimo

info
^^^^
Get info for a timer

Usage
    !timer info ``<name>``

Example
    Output the details for the ``social`` timer::

        !timer info social

list
^^^^
List timers

Usage
    !timer list

Example
    List timers available in Botisimo::

        !timer list

new
^^^
Create a new timer

Usage
    !timer new ``<name>`` ``<interval>`` ``<message>``

Example
    Create a new timer named ``social`` that posts the message every 5 minutes in the current channel::

        !timer new social 5 Follow me on twitter @botisimo

start
^^^^^
Starts a timer in the current channel

Usage
    !timer start ``<name>``

Example
    Start the timer named ``social`` in the current channel::

        !timer start social

stop
^^^^
Stops a timer

Usage
    !timer stop ``<name>``

Example
    Stop the timer named ``social`` but does not delete it::

        !timer stop social
