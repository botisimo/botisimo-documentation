$[discord role add]
===================

Adds a role to the user issuing the command.

Usage:
    $[discord role add ``<role>`` ``[user]``]

Arguments:
    * ``role`` **<required>** - URL encoded role name (ex: ``$(urlencode My Awesome Role)``)
    * ``user`` **[optional]** - Discord user to add the role to

Example Command:
    **name**: !awesome

    **response**: $[discord role add $(urlencode My Awesome Role)] You have been added to the My Awesome Role role

    **output**::

        user:     !awesome
        botisimo: You have been added to the My Awesome Role role

$[discord role check]
=====================

Requires a user to have a discord role.

Usage:
    $[discord role check ``<role>``]

Arguments:
    * ``role`` **<required>** - URL encoded role name (ex: ``$(urlencode My Awesome Role)``)

Example Command:
    **name**: !expelliarmus

    **response**: $[discord role check $(urlencode My Awesome Role)] (∩｀-´)⊃━☆ﾟ.*･｡ﾟ

    **output**::

        user:     !expelliarmus
        botisimo: (∩｀-´)⊃━☆ﾟ.*･｡ﾟ

$[discord role remove]
======================

Removes a role from the user issuing the command.

Usage:
    $[discord role remove ``<role>`` ``[user]``]

Arguments:
    * ``role`` **<required>** - URL encoded role name (ex: ``$(urlencode My Awesome Role)``)
    * ``user`` **[optional]** - Discord user to remove the role from

Example Command:
    **name**: !notawesome

    **response**: $[discord role remove $(urlencode My Awesome Role)] You have been removed from the My Awesome Role role

    **output**::

        user:     !notawesome
        botisimo: You have been removed from the My Awesome Role role
