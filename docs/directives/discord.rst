$[discord role add]
===================

Adds a role to the user issuing the command.

Usage
    $[discord role add ``<role>``]

Example
    Add a user to the wizard role and responds::

        $[discord role add wizard] You have been added to the wizard role

    ``!wizard`` -> ``You have been added to the wizard role``

$[discord role check]
=====================

Requires a user to have a discord role.

Usage
    $[discord role check ``<role>``]

Example
    Check that a user has the wizard role and responds if they do::

        $[discord role check wizard] (∩｀-´)⊃━☆ﾟ.*･｡ﾟ

    ``!expelliarmus`` -> ``(∩｀-´)⊃━☆ﾟ.*･｡ﾟ``

$[discord role remove]
======================

Removes a role from the user issuing the command.

Usage
    $[discord role remove ``<role>``]

Example
    Remove the user from the wizard role and responds::

        $[discord role remove wizard] You have been removed from the wizard role

    ``!muggle`` -> ``You have been removed from the wizard role``
