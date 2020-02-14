$[discord role add]
===================

Adds a role to the user issuing the command.

Usage:
    $[discord role add ``<role>`` ``[user]``]

Arguments:
    * ``role`` **<required>** - URL encoded role name
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
    * ``role`` **<required>** - URL encoded role name

Options:
    * ``-p, --public`` **[optional]** - If present then error message will be sent to public chat (instead of direct message)
    * ``-s, --silent`` **[optional]** - If present then no error message will be sent
    * ``--error-message <message>`` **[optional]** - URL encoded error message

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
    * ``role`` **<required>** - URL encoded role name
    * ``user`` **[optional]** - Discord user to remove the role from

Example Command:
    **name**: !notawesome

    **response**: $[discord role remove $(urlencode My Awesome Role)] You have been removed from the My Awesome Role role

    **output**::

        user:     !notawesome
        botisimo: You have been removed from the My Awesome Role role
