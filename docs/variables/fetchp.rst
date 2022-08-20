$(fetchp)
=========

Resolves the response from the url using a POST request. Similar to :doc:`$(fetch) </variables/fetch>`.

.. note::

    To avoid hitting any rate limits against remote APIs, all responses are cached for 5 seconds.

Usage:
    $(fetchp ``<url>`` ``[data]`` ``[path]``)

Arguments:
    * ``url`` **<required>** - The url to send the request to
    * ``data`` **[optional]** - The data string to send to the url
    * ``path`` **[optional]** - The path to the property in the response (JSON only)

Example Command:
    **name**: !dadjoke

    **response**: $(fetchp https://icanhazdadjoke.com/graphql query=$(urlencode query { joke {id joke permalink } }) data.joke.joke)

    **output**::

        user:     !dadjoke
        botisimo: Why are skeletons so calm? Because nothing gets under their skin.
