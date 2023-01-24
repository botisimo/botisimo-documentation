Webhooks
========

Botisimo uses webhooks to notify your application when an event happens in your team member accounts. Webhooks are particularly useful for asynchronous events like when a team member updates their account or a stream goes live.

.. note:: Ready to go live? `Register your webhook integration URL <https://botisimo.com/team/integrations>`_ so Botisimo knows where to deliver events.

How Botisimo uses Webhooks
--------------------------

A webhook enables Botisimo to push real-time notifications to your app. Botisimo uses HTTPS to send these notifications to your app as a JSON payload. You can then use these notifications to execute actions in your backend systems.

Steps to receive webhooks
-------------------------

You can start receiving event notifications in your app using the steps in this section:

#. Identify the events you want to monitor and the event payloads to parse.
#. Create a webhook endpoint as an HTTP endpoint (URL) on your local server.
#. Handle requests from Botisimo by parsing each event object and returning 2xx response status codes.
#. Deploy your webhook endpoint so it's a publicly accessible HTTPS URL.
#. Register your publicly accessible HTTPS URL in the Botisimo integration dashboard.

Handle requests from Botisimo
-----------------------------

Your endpoint must be configured to read objects for the type of notifications you want to receive. Botisimo sends events to your webhook endpoint as part of a POST request with a JSON payload.

Check event objects
^^^^^^^^^^^^^^^^^^^

Each event is structured as an object with a eventType, id, and related Botisimo resource nested under data. Your endpoint must check the eventType and parse the payload of each event.

.. code-block:: js

   {
      "messageId": "20612112-0305-46a9-a67a-e3ffc5bb7a18",
      "timestamp": 1674489999154,
      "eventType": "account.updated",
      "data": { ... }
   }

Return a 2xx response
^^^^^^^^^^^^^^^^^^^^^

Your endpoint must quickly return a successful status code (2xx) prior to any complex logic that could cause a timeout. For example, you must return a 200 response before updating a team member's account in your system.

Built-in retries
^^^^^^^^^^^^^^^^

Botisimo webhooks have built-in retry methods for 3xx, 4xx, or 5xx response status codes. If Botisimo doesn't quickly receive a 2xx response status code for an event, we mark the event as failed and stop trying to send it to your endpoint. After multiple days, we email you about the misconfigured endpoint, and automatically disable it soon after if you haven't addressed it.

Event Types
-----------

- ``account.created``
- ``account.updated``
- ``account.discord.updated``
- ``account.slack.updated``
- ``account.custom_bot.updated``
- ``account.custom_bot.updated.twitch``
- ``account.custom_bot.updated.youtube``
- ``account.custom_bot.updated.facebook``
- ``account.custom_bot.updated.trovo``
- ``account.custom_bot.updated.dlive``
- ``account.custom_bot.updated.brime``
- ``account.custom_bot.updated.zoom``
- ``account.custom_bot.updated.twitter``
- ``account.custom_bot.updated.tiktok``
- ``connection.created``
- ``connection.created.twitch``
- ``connection.created.youtube``
- ``connection.created.facebook``
- ``connection.created.trovo``
- ``connection.created.dlive``
- ``connection.created.brime``
- ``connection.created.zoom``
- ``connection.created.twitter``
- ``connection.created.tiktok``
- ``connection.updated``
- ``connection.updated.twitch``
- ``connection.updated.youtube``
- ``connection.updated.facebook``
- ``connection.updated.trovo``
- ``connection.updated.dlive``
- ``connection.updated.brime``
- ``connection.updated.zoom``
- ``connection.updated.twitter``
- ``connection.updated.tiktok``
- ``connection.deleted``
- ``connection.deleted.twitch``
- ``connection.deleted.youtube``
- ``connection.deleted.facebook``
- ``connection.deleted.trovo``
- ``connection.deleted.dlive``
- ``connection.deleted.brime``
- ``connection.deleted.zoom``
- ``connection.deleted.twitter``
- ``connection.deleted.tiktok``
- ``connection.stream.started``
- ``connection.stream.started.twitch``
- ``connection.stream.started.youtube``
- ``connection.stream.started.facebook``
- ``connection.stream.started.trovo``
- ``connection.stream.started.dlive``
- ``connection.stream.started.brime``
- ``connection.stream.started.tiktok``
- ``connection.stream.ended``
- ``connection.stream.ended.twitch``
- ``connection.stream.ended.youtube``
- ``connection.stream.ended.facebook``
- ``connection.stream.ended.trovo``
- ``connection.stream.ended.dlive``
- ``connection.stream.ended.brime``
- ``connection.stream.ended.tiktok``
- ``stream_report.created``
- ``creator_site.updated``
- ``stream_frame.updated``
- ``stream_overlays.updated``
- ``spam_filter.updated``
- ``music.updated``
- ``command.created``
- ``command.updated``
- ``command.deleted``
- ``giveaway.created``
- ``giveaway.updated``
- ``giveaway.deleted``
- ``giveaway.winner.created``
- ``poll.created``
- ``poll.updated``
- ``poll.deleted``
- ``poll.winner.created``
- ``event.created``
- ``event.updated``
- ``event.deleted``
- ``shop_item.created``
- ``shop_item.updated``
- ``shop_item.deleted``
- ``shop_item.purchase.redeemed``
- ``shop_item.purchase.refunded``
- ``video.created``
- ``video.updated``
- ``video.deleted``
- ``timer.created``
- ``timer.updated``
- ``timer.deleted``
