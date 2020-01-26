DyneOps
=======

DyneOps is a fun chat game that will test your memory and put your 10-key numpad typing skills to the test. This page defines some important terms and concepts to understand to be able to play DyneOps.

If you are a streamer and you have Botisimo in your channel, you can `enable DyneOps here <https://botisimo.com/account/dyneops>`_.

.. note::

    If viewers are not receiving whispers from Botisimo in Twitch, they may need to send it a whisper first to get it working for their account.

Dyne
^^^^

Dynes are the main aspect of DyneOps. They are found randomly when chatting with other viewers in chat and each viewer can generate a Dyne using the command ``!dyne`` in chat every 60 minutes. Most Dynes contain `Goldfrags <#goldfrags>`_ and some Dynes contain `decryption chips <#decryption-chips>`_ that are used to more easily unlock more Dynes. To retrieve the loot from a Dyne you must successfully perform the `TranceDecryption <#dyne-trancedecryption>`_ process.

.. note::

    Viewers that are subscribed to the streamer will be able to generate a Dyne every 30 minutes.

Dyne TranceDecryption
^^^^^^^^^^^^^^^^^^^^^

TranceDecryption is the process of unlocking a Dyne to get the loot out of it. Once you have found or generated a Dyne Botisimo will notify you::

    Botisimo: @viewer1 You intercepted a Dyne! Start TranceDecryption now! BudStar !start !readme [5 min remain]

Once you have been notified of the Dyne you will have 5 minutes to start the decryption before the Dyne corrupts. To start TranceDecryption type ``!start`` in the chat::

    viewer1: !start

Shortly after you start the TranceDecryption, Botisimo will relay you the Synapse for decryption::

    Botisimo: @viewer1 Your Synapse is '##(@)*4&0&^7*9*((421(\'. Remove symbols and give me only numbers! [10 sec remain]

After starting TranceDecryption you will have 10 seconds to return the numbers from the Synapse in the exact order they are in before the Dyne is corrupted::

    viewer1: 4079421

Botisimo will alert you whether your TranceDecryption was a success or not and fetch your loot if successful::

    Botisimo: @viewer1 TranceDecryption success! PogChamp PogChamp PogChamp You found 6 Goldfrags - completed in 7 seconds

That's it, now you're ready to TranceDecrypt Dyne!

HYPERDyne
^^^^^^^^^

Sometimes a Dyne will appear as a HYPERDyne. HYPERDynes are very similar to regular Dynes but they have more loot and they are longer and you have to sort the numbers from lowest to highest when doing `TranceDecryption <#hyperdyne-trancedecryption>`_.

HYPERDyne TranceDecryption
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have found or generated a HYPERDyne Botisimo will notify you::

    Botisimo: @viewer1 You intercepted a HYPERDyne! Start TranceDecryption now! BudStar !start !readme [5 min remain]

Once you have been notified of the HYPERDyne you will have 5 minutes to start the decryption before the HYPERDyne corrupts. To start TranceDecryption type ``!start`` in the chat::

    viewer1: !start

Shortly after you start the TranceDecryption, Botisimo will relay you the Synapse for decryption::

    Botisimo: @viewer1 Your Synapse is '##(@)*4&0&^7*9*((421(\&3^8))'. Remove symbols and give me the numbers IN ASCENDING ORDER (lowest to highest)! [10 sec remain]

After starting TranceDecryption you will have 10 seconds to return the numbers from the Synapse sorted from lowest to highest before the Dyne is corrupted::

    viewer1: 012344789

Botisimo will alert you whether your TranceDecryption was a success or not and fetch your loot if successful::

    Botisimo: @viewer1 TranceDecryption success! PogChamp PogChamp PogChamp You found 12 Goldfrags - completed in 9 seconds

That's it, now you're ready to TranceDecrypt HYPERDynes!

Goldfrags
^^^^^^^^^

Goldfrags are the currency of DyneOps and can be gained randomly as you chat or by unlocking Dynes. Viewers can exchange their currency for items in the `Shop <#shop>`_. If you are a streamer using Botisimo you can `change the currency name here <https://botisimo.com/account/settings>`_.

Shop
^^^^

The Shop is where viewers can exchange their currency for items created by the streamer. To view the shop, type ``!shop`` in the chat::

    viewer1: !shop

Botisimo will display the shop items in chat::

    Botisimo: Streamer's Shop - 1. Dance (500 Goldfrags) 2. Song Request (250 Goldfrags) - More info https://botisimo.com/u/streamer/shop

Each item will have a corresponding number that you can use to buy it using the ``!buy <key>`` command::

    viewer1: !buy 2

If you have enough currency to buy the item, Botisimo will announce the purchase in chat to let the streamer know::

    Botisimo: @streamer TwitchRPG TwitchRPG TwitchRPG @viewer1 has purchased Song Request!

If you are a streamer, you can `configure your shop here <https://botisimo.com/account/shop>`_.

Decryption Chips
^^^^^^^^^^^^^^^^

Decryption Chips assist you during TranceDecryption and can be found by opening Dynes or merging. You can hold a maximum of 3 of each item.

> Noobuster
-----------

A noobuster increases the amount of time you have to complete the TranceDecryption by 1. So if you have 1 noobuster then you will have 11 seconds instead of 10 to complete the TranceDecryption.

> Syncswitch
------------

A syncswitch decreases the numbers you have to return for a successful TranceDecryption by 1. So if you have 1 syncswitch and the synapse is ``##(@)*4&0&^7*9*((421(\`` then you only have to return ``407942`` instead of ``4079421`` for the TranceDecryption to be successful. if you have 3 syncswitches and the synapse is ``##(@)*4&0&^7*9*((421(\`` then you only have to return ``4079`` instead of ``4079421`` for the TranceDecryption to be successful.

> Skullshunt
------------

A set of 3 skullshunts will auto-sort your HyperDyne Synapse before you have to decrypt it. So if you have 3 skullshunts and you find a HyperDyne then you do not need to sort the numbers when doing the TranceDecryption because they will already be sorted for you. example: ``##(@)*0&1&^2*3*((447(\&8^9))``.

**How to acquire Decryption Chips:**

- ``Noobuster`` - Increases decryption time by 1 second

    - Successful TranceDecryption
    - Purchase in shop for 1,000 currency "!buy noobuster"

- ``Syncswitch`` - Decrease required numbers by 1 during TranceDecryption

    - Successful TranceDecryption
    - Merge 3 Noobusters "!merge noobusters"
    - Purchase in shop for 4,500 currency "!buy syncswitch"

- ``Skullshunt`` - Set of 3 Skullshunts will auto-sort your Synapse decryption if needed

    - Merge 3 Syncswitches "!merge syncswitches"
    - Purchase in shop for 16,000 currency "!buy skullshunt"

Commands
^^^^^^^^

- ``!buy <key>`` - Purchase an item from the shop using currency
- ``!dyne`` - Generate a Dyne (can be used 1 time per 60 minutes, 30 minutes for subscribers)
- ``!give <amount> <username> [username=] ...`` - Give some currency to 1 or more users (amount should be a number or the word "dyne") **[mods only]**
- ``!inventory`` - Receive inventory (currency, decryption chips, etc.) info via whisper
- ``!leaders`` - Display link to leaderboard in chat
- ``!merge <item>`` - Merge 3 items into a better item (valid items: noobuster, syncswitch, skullshunt)
- ``!optin`` - Opt in to DyneOps announcements for your user
- ``!optout`` - Opt out of DyneOps announcements for your user
- ``!readme`` - Display link to these docs
- ``!shop`` - Display available shop items in chat
- ``!start`` - Start a TranceDecryption for a Dyne
- ``!stats`` - Receive stats via whisper
