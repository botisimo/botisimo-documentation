$[transfer]
===========

Directs the bot to transfer currency from the user who uses the command to the targeted user.

Usage
    $[transfer ``<amount>`` ``<target>``]

Example
    Transfer ``100`` currency from the user when they use the command and outputs the response::

        $[transfer 100 $(1)] You just transferred 100 Goldfrags to $(1) for using this command, woo!

    ``!transfer @username`` -> ``You just transferred 100 Goldfrags to @username for using this command, woo!``

    If the user does not have enough currency they will receive a direct message explaining

    ``!transfer @username`` -> ``Not enough Goldfrags to use that command 37/100``
