$(winner)
=========

Resolve the username as a mention of a random user currently online in the channel.

Usage:
    $(winner ``[minutes=10]`` ``[keyword=]``)

Arguments:
    * ``minutes`` **[optional]** - The number of minutes to look back in chat for the keyword
    * ``keyword`` **[optional]** - The keyword to qualify to be selected as a winner (if no keyword then any text will qualify)

Example Command:
    **name**: !winner

    **response**: The winners is $(winner 5 enter)!

    **output**::

        user:     !winner
        botisimo: The winner is @bob!
