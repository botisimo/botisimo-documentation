Memberships API
===============

- `List Memberships`_
- `Read Membership`_

List Memberships
----------------

List available memberships

- **GET** /membership/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/membership/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=========================== ======== =================================================
Field                       Type     Description
=========================== ======== =================================================
memberships                 object[]
memberships.id              number   The ID of the membership
memberships.name            string   The name of the membership
memberships.description     string   The membership description
memberships.priceMonth      number   The cost of the membership per month in cents
memberships.priceYear       number   The cost of the membership per year in cents
memberships.gold            number   The price in loyalty points to redeem
memberships.goldMultiplier  number   The loyalty points multiplier for this membership
memberships.resourceId      number   The resource ID of the membership image
memberships.badgeResourceId number   The resource ID of the membership badge
=========================== ======== =================================================

Read Membership
---------------

Read membership details

- **GET** /membership/:id

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/membership/1', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

========================== ====== =================================================
Field                      Type   Description
========================== ====== =================================================
membership                 object
membership.id              number The ID of the membership
membership.name            string The name of the membership
membership.description     string The membership description
membership.priceMonth      number The cost of the membership per month in cents
membership.priceYear       number The cost of the membership per year in cents
membership.goldMultiplier  number The loyalty points multiplier for this membership
membership.resourceId      number The resource ID of the membership image
membership.badgeResourceId number The resource ID of the membership badge
========================== ====== =================================================
