$(countdown)
============

Resolves the time between now and the given date.

Usage:
    $(countdown ``<date>`` ``[time]``)

Arguments:
    * ``date`` **<required>** - The date to compare (ex: 12/25/2020)
    * ``time`` **[optional]** - The time of day (ex: 12:30pm)

Example Command:
    **name**: !countdown

    **response**: The new year begins in $(countdown 1/1/2021 00:00:00)

    **output**::

        user:     !countdown
        botisimo: The new year begins in 360 days 12 hours 37 minutes
