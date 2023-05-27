$(ai)
======

AI generated response based on context and prompt.

Must have a Pro membership and at least $1 balance in your account. `Manage my balance <https://botisimo.com/account/billing>`_

Usage:
    $(ai ``<context>`` | ``<prompt>``)

Arguments:
    * ``context`` **<required>** - The context of the AI to use for the response
    * ``prompt`` **<required>** - The prompt to send to the AI to generate a response

Example Command:
    **name**: !rng

    **response**: $(ai writing a haiku | pick a random number between 1 and 100)

    **output**::

        user:     !rng
        botisimo: From one to hundred, An answer must be chosen, Sixty-four it is.

Example Command:
    **name**: hey billy

    **response**: $(ai billy the kid | $(query))

    **output**::

        user:     hey billy how did you get your name?
        botisimo: Well, I got my name from my birth name William H. Bonney. But folks started calling me Billy the Kid because of my young age and my perceived innocent looks. Some people say that I was a kid when I started my outlaw life, but truth be told, I was only 21 years old when I was killed.
