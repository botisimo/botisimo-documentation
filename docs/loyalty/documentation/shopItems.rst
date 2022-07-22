Shop Items API
==============

- `List Shop Items`_
- `Read Shop Item`_
- `Redeem Shop Item`_

List Shop Items
---------------

List available shop items

- **GET** /shopItem/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/shopItem/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

======================= ======== =======================================
Field                   Type     Description
======================= ======== =======================================
shopItems               object[]
shopItems.id            number   The ID of the shop item
shopItems.name          string   The name of the shop item
shopItems.description   string   The shop item description
shopItems.type          string   The shop item type
shopItems.price         number   The price in loyalty points to redeem
shopItems.quantity      number   The quantity available
shopItems.resourceId    number   The resource ID of the shop item image
shopItems.loyaltyTierId number   The minimum loyalty tier required
shopItems.tags          object[] List of tags
shopItems.tags.id       number   The ID of the tag
shopItems.tags.name     string   The name of the tag
======================= ======== =======================================

Read Shop Item
--------------

Read shop item details

- **GET** /shopItem/:id

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/shopItem/1', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

====================== ======== =======================================
Field                  Type     Description
====================== ======== =======================================
shopItem               object
shopItem.id            number   The ID of the shop item
shopItem.name          string   The name of the shop item
shopItem.description   string   The shop item description
shopItem.type          string   The shop item type
shopItem.price         number   The price in loyalty points to redeem
shopItem.quantity      number   The quantity available
shopItem.resourceId    number   The resource ID of the shop item image
shopItem.loyaltyTierId number   The minimum loyalty tier required
shopItem.tags          object[] List of tags
shopItem.tags.id       number   The ID of the tag
shopItem.tags.name     string   The name of the tag
====================== ======== =======================================

Redeem Shop Item
----------------

Redeem shop item

- **PUT** /shopItem/:id/redeem

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.put('https://botisimo.com/api/v1/loyalty/:team/shopItem/1/redeem', {}, {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

====================== ======== =======================================
Field                  Type     Description
====================== ======== =======================================
shopItem               object
shopItem.id            number   The ID of the shop item
shopItem.name          string   The name of the shop item
shopItem.description   string   The shop item description
shopItem.type          string   The shop item type
shopItem.price         number   The price in loyalty points to redeem
shopItem.quantity      number   The quantity available
shopItem.resourceId    number   The resource ID of the shop item image
shopItem.loyaltyTierId number   The minimum loyalty tier required
shopItem.tags          object[] List of tags
shopItem.tags.id       number   The ID of the tag
shopItem.tags.name     string   The name of the tag
====================== ======== =======================================
