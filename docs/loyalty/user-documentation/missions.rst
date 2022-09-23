Missions API
============

- `List Missions`_
- `Read Mission`_
- `Complete Mission`_

List Missions
-------------

List available missions

- **GET** /mission/list

Mission type can be: ``follow``, ``profile``, ``connections``, ``platform``, ``media``, ``code``, ``qr-code``

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/mission/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

==================== ======== =======================================
Field                Type     Description
==================== ======== =======================================
missions             object[]
missions.id          number   The ID of the mission
missions.name        string   The name of the mission
missions.description string   The mission description
missions.type        string   The mission type
missions.reward      number   The number of loyalty points rewarded
missions.resourceId  number   The resource ID of the mission image
missions.tags        object[] List of tags
missions.tags.id     number   The ID of the tag
missions.tags.name   string   The name of the tag
==================== ======== =======================================

Read Mission
------------

Read mission details

- **GET** /mission/:id

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/mission/1', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=================== ======== =======================================
Field               Type     Description
=================== ======== =======================================
mission             object
mission.id          number   The ID of the mission
mission.name        string   The name of the mission
mission.description string   The mission description
mission.type        string   The mission type
mission.reward      number   The number of loyalty points rewarded
mission.resourceId  number   The resource ID of the mission image
mission.tags        object[] List of tags
mission.tags.id     number   The ID of the tag
mission.tags.name   string   The name of the tag
=================== ======== =======================================

Complete Mission
----------------

Complete mission

- **PUT** /mission/:id/complete

Request

=========== ======== =============================================
Field       Type     Description
=========== ======== =============================================
code        [string] Required if ``code`` mission
=========== ======== =============================================

.. code-block:: js

   const response = await axios.put('https://botisimo.com/api/v1/loyalty/:team/mission/1/redeem', {}, {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=================== ======== =======================================
Field               Type     Description
=================== ======== =======================================
mission             object
mission.id          number   The ID of the mission
mission.name        string   The name of the mission
mission.description string   The mission description
mission.type        string   The mission type
mission.reward      number   The number of loyalty points rewarded
mission.resourceId  number   The resource ID of the mission image
mission.tags        object[] List of tags
mission.tags.id     number   The ID of the tag
mission.tags.name   string   The name of the tag
=================== ======== =======================================
