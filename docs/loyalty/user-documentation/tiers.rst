Tiers API
=========

- `List Tiers`_
- `Read Tier`_

List Tiers
----------

List available tiers

- **GET** /tier/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/tier/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

===================== ======== =======================================
Field                 Type     Description
===================== ======== =======================================
tiers                 object[]
tiers.id              number   The ID of the tier
tiers.name            string   The name of the tier
tiers.description     string   The tier description
tiers.gold            number   The points required to achieve tier
tiers.resourceId      number   The resource ID of the tier image
tiers.badgeResourceId number   The resource ID of the tier badge
===================== ======== =======================================

Read Tier
---------

Read tier details

- **GET** /tier/:id

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/tier/1', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

==================== ====== =======================================
Field                Type   Description
==================== ====== =======================================
tier                 object
tier.id              number The ID of the tier
tier.name            string The name of the tier
tier.description     string The tier description
tier.gold            number The points required to achieve tier
tier.resourceId      number The resource ID of the tier image
tier.badgeResourceId number The resource ID of the tier badge
==================== ====== =======================================
