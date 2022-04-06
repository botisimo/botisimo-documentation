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

Response

=================== ======== =======================================
Field               Type     Description
=================== ======== =======================================
events              object[]
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

Response

================== ======== ==================================================
Field              Type     Description
================== ======== ==================================================
event              object
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
