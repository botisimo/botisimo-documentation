Advanced Example
================

This example shows you how to combine the ``$(fetch)``, ``$(urlencode)``, and ``$(query)`` response variables to make a !ascii command that translates the user's input into formatted ASCII text for Discord.

Example Command:
    **command**: !ascii

    **response**: \`\`\`$(fetch http://artii.herokuapp.com/make?text=$(urlencode $(query))&font=colossal)\`\`\`

    **output**::

        user:     !ascii Hello World
        botisimo: 888    888          888 888              888       888                  888      888
                  888    888          888 888              888   o   888                  888      888
                  888    888          888 888              888  d8b  888                  888      888
                  8888888888  .d88b.  888 888  .d88b.      888 d888b 888  .d88b.  888d888 888  .d88888
                  888    888 d8P  Y8b 888 888 d88""88b     888d88888b888 d88""88b 888P"   888 d88" 888
                  888    888 88888888 888 888 888  888     88888P Y88888 888  888 888     888 888  888
                  888    888 Y8b.     888 888 Y88..88P     8888P   Y8888 Y88..88P 888     888 Y88b 888
                  888    888  "Y8888  888 888  "Y88P"      888P     Y888  "Y88P"  888     888  "Y88888

This example shows you how to combine the ``$(ai)`` and ``$(query)`` response variables to make an AI generated response command takes on the persona of Billy the Kid.

Example Command:
    **command**: hey billy

    **response**: $(ai billy the kid | $(query))

    **output**::

        user:     hey billy how did you get your name?
        botisimo: Well, I got my name from my birth name William H. Bonney. But folks started calling me Billy the Kid because of my young age and my perceived innocent looks. Some people say that I was a kid when I started my outlaw life, but truth be told, I was only 21 years old when I was killed.
