$[event]
========

Sends a custom event to the `events overlay <https://botisimo.com/account/overlays>`_.

Usage:
    $[event]

Options:
    * ``-t, --text <text>`` **[optional]** - URL encoded primary text for the event
    * ``-s, --secondary-text <text>`` **[optional]** - URL encoded secondary text for the event
    * ``-d, --duration <milliseconds>`` **[optional]** - Duration in milliseconds to display event
    * ``-i, --image <url>`` **[optional]** - URL for image to display for event
    * ``-a, --audio <url>`` **[optional]** - URL to audio to play for event

Example Command:
    **name**: !event

    **response**: $[event -t $(urlencode This is the primary text) -s $(urlencode This is the secondary text) -d 5000 -i https://media2.giphy.com/media/KXtq8oYQrYMIF9Esi7/giphy.gif -a http://soundbible.com/grab.php?id=1817&type=mp3] event sent

    **output**::

        user:     !event
        botisimo: event sent
