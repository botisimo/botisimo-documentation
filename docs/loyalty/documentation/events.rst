Events API
==========

- `List Events`_
- `Read Event`_

List Events
-----------

List scheduled events

- **GET** /event/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/event/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=================== ======== =======================================
Field               Type     Description
=================== ======== =======================================
events              object[]
events.id           number   The ID of the event
events.name         string   The name of the event
events.description  string   The event description
events.url          string   The event URL
events.callToAction string   The label for the call to action button
events.location     string   The location of the event
events.start        number   Unix timestamp of start of event
events.end          number   Unix timestamp of end of event
events.status       string   Status of the event (completed, upcoming, ongoing)
events.resourceId   number   The resource ID of the event image
events.tags         object[] List of tags
events.tags.id      number   The ID of the tag
events.tags.name    string   The name of the tag
=================== ======== =======================================

Read Event
----------

Read event details

- **GET** /event/:id

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/event/1', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

================== ======== ==================================================
Field              Type     Description
================== ======== ==================================================
event              object
event.id           number   The ID of the event
event.name         string   The name of the event
event.description  string   The event description
event.url          string   The event URL
event.callToAction string   The label for the call to action button
event.location     string   The location of the event
event.start        number   Unix timestamp of start of event
event.end          number   Unix timestamp of end of event
event.status       string   Status of the event (completed, upcoming, ongoing)
event.resourceId   number   The resource ID of the event image
event.tags         object[] List of tags
event.tags.id      number   The ID of the tag
event.tags.name    string   The name of the tag
================== ======== ==================================================

Example

.. code-block:: js

   {
      "event": {
         "status": "completed",
         "id": 6,
         "name": "OpTic Major 1 Tournament",
         "description": "Tickets Are Now Available for the OpTic Major I",
         "callToAction": "GET TICKETS",
         "url": "https://www.tixr.com/groups/optictexas/events/optic-texas-major-i-35567",
         "location": "Esports Stadium Arlington",
         "start": 1649008800,
         "end": 1649296800,
         "resourceId": 6681,
         "createdAt": "2022-03-16T03:15:21.000Z",
         "updatedAt": "2022-03-16T03:17:56.000Z",
         "tags": []
      }
   }
