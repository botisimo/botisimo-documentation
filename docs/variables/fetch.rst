$(fetch)
========

Resolves the response from the url using a GET request.

.. note::

    To avoid hitting any rate limits against remote APIs, all responses are cached for 5 seconds.

Usage:
    $(fetch ``<url>``)

Arguments:
    * ``url`` **<required>** - The url to send the request to
    * ``path`` **[optional]** - The path to the property in the response (JSON only)

Example Command:
    **name**: !kanye

    **response**: $(fetch https://api.kanye.rest/ quote) - Kanye

    **output**::

        user:     !kanye
        botisimo: I'm a creative genius - Kanye
