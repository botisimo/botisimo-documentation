Tiers API
=========

- `List Tiers`_
- `Read Tier`_
- `Unlock Tier`_

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
tiers.priceMonth      number   The cost of the tier per month in cents
tiers.priceYear       number   The cost of the tier per year in cents
tiers.gold            number   The price in loyalty points to redeem
tiers.goldMultiplier  number   The loyalty points multiplier for this tier
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
tier.priceMonth      number The cost of the tier per month in cents
tier.priceYear       number The cost of the tier per year in cents
tier.gold            number The price in loyalty points to redeem
tier.goldMultiplier  number The loyalty points multiplier for this tier
tier.resourceId      number The resource ID of the tier image
tier.badgeResourceId number The resource ID of the tier badge
==================== ====== =======================================

Unlock Tier
-----------

Unlock tier

- **PUT** /tier/:id/unlock

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.put('https://botisimo.com/api/v1/loyalty/:team/tier/1/unlock', {}, {
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
tier.priceMonth      number The cost of the tier per month in cents
tier.priceYear       number The cost of the tier per year in cents
tier.gold            number The price in loyalty points to redeem
tier.goldMultiplier  number The loyalty points multiplier for this tier
tier.resourceId      number The resource ID of the tier image
tier.badgeResourceId number The resource ID of the tier badge
==================== ====== =======================================
