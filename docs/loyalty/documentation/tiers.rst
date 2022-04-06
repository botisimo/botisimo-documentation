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

Response

===================== ======== =======================================
Field                 Type     Description
===================== ======== =======================================
tiers                 object[]
tiers.name            string   The name of the tier
tiers.description     string   The tier description
tiers.gold            number   The price in loyalty points to redeem
tiers.resourceId      number   The resource ID of the tier image
tiers.badgeResourceId number   The resource ID of the tier image
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

Response

===================== ====== =======================================
Field                 Type   Description
===================== ====== =======================================
tier                  object
tiers.name            string The name of the tier
tiers.description     string The tier description
tiers.gold            number The price in loyalty points to redeem
tiers.resourceId      number The resource ID of the tier image
tiers.badgeResourceId number The resource ID of the tier image
===================== ====== =======================================

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

Response

===================== ====== =======================================
Field                 Type   Description
===================== ====== =======================================
tier                  object
tiers.name            string The name of the tier
tiers.description     string The tier description
tiers.gold            number The price in loyalty points to redeem
tiers.resourceId      number The resource ID of the tier image
tiers.badgeResourceId number The resource ID of the tier image
===================== ====== =======================================
