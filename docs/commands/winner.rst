!winner
=======

Pick a random winner from chat who sent a message in last 10 minutes. Optionally, use the ``message`` to filter users who typed a specific message (default: any message). You can also alter the minutes by using the ``|`` character followed by a number (example: ``!winner enter|30``).

Usage:
    !winner ``[message]`` ``[|minutes]``

Example:
    ::

        user:     type "go for the win" to qualify
        bob:      go for the win
        user:     !winner go for the win|5
        botisimo: ​@bob wins!
