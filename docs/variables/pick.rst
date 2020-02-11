$(pick)
=======

Resolves a random response from the given options.

Usage:
    $(pick ``<option>`` | ``[option]`` | ``[option]`` | ...)

Arguments:
    * ``option`` **<required>** - The message to display in chat (to add multiple options separate with a ``|`` character)

Example Command:
    **name**: !pick

    **response**: I'm thinking...$(pick yes | no | maybe so | I don't know)

    **output**::

        user:     !pick
        botisimo: I'm thinking...maybe so
        user:     !pick
        botisimo: I'm thinking...yes
