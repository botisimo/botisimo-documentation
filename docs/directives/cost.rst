$[cost]
=======

Directs the bot to add a currency cost to the command.

Usage
    $[cost ``<amount>``]

Example
    Add a cost of ``50`` currency to use the command and outputs the response::

        $[cost 50] You just paid 50 Goldfrags to use this command, ha!

    ``!cost`` -> ``You just paid 50 Goldfrags to use this command, ha!``

    If the user does not have enough currency they will receive a direct message explaining

    ``!cost`` -> ``Not enough Goldfrags to use that command 37/50``
