$[discord role add]
===================

Adds a role to the user issuing the command.

Usage:
    $[discord role add ``<role>``]

Example Command:
    **name**: !wizard

    **response**: $[discord role add wizard] You have been added to the wizard role

    **output**::

        user:     !wizard
        botisimo: You have been added to the wizard role

$[discord role check]
=====================

Requires a user to have a discord role.

Usage:
    $[discord role check ``<role>``]

Example Command:
    **name**: !expelliarmus

    **response**: $[discord role check wizard] (∩｀-´)⊃━☆ﾟ.*･｡ﾟ

    **output**::

        user:     !expelliarmus
        botisimo: (∩｀-´)⊃━☆ﾟ.*･｡ﾟ

$[discord role remove]
======================

Removes a role from the user issuing the command.

Usage:
    $[discord role remove ``<role>``]

Example Command:
    **name**: !muggle

    **response**: $[discord role remove wizard] You have been removed from the wizard role

    **output**::

        user:     !muggle
        botisimo: You have been removed from the wizard role
