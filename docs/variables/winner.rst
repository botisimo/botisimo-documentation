$(winner)
=========

Resolve the username as a mention of a random user currently online in the channel.

Usage
    $(winner ``[minutes=10]`` ``[keyword=]``)

Example
    Output a randomly selected user who is online and sent the message ``enter`` in the last 5 minutes. The keyword is case sensitive::

        The winners is $(winner 5 enter)!

    ``!winner`` -> ``The winner is @gary!``
