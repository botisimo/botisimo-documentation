$[event]
========

Sends a custom event to the `events overlay <https://botisimo.com/account/overlays>`_.

Usage:
    $[event ``[text]`` | ``[subtext]`` | ``[milliseconds=3000]`` | ``[thumbnail]`` | ``[sound]``]

Example Command:
    **name**: !event

    **response**: $[event This is the text | This is the subtext | 5000 | https://media2.giphy.com/media/KXtq8oYQrYMIF9Esi7/giphy.gif | http://soundbible.com/grab.php?id=1817&type=mp3] event sent

    **output**::

        user:     !event
        botisimo: event sent
