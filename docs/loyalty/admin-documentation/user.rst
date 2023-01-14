User API
========

- `Get User`_
- `Add Points`_
- `Delete User`_

Get User
--------

Get or create a user by email address

- **GET** /user

Request

=========== ======== =============================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================
id          string   The SSO identifier of the user, usually an internal ID from your system
email       string   The email address of the user
tags        string   Comma separated list of tag IDs
=========== ======== =============================================================================================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/admin/user', {
      params: {
         id: '1234567890',
         email: 'joe.someone@example.com',
      },
      headers: {
         'client-id': 'xxxxx-xxxxx-xxxxx-xxxxx',
      },
   });

Response

================================= ======== =================================================================================
Field                             Type     Description
================================= ======== =================================================================================
user                              object   Information about the logged in user
user.avatar                       string   URL to to user avatar
user.createdAt                    string   When the user was created
user.dateOfBirth                  string   Date of birth formatted as ``MM/DD/YYYY``
user.gold                         number   Number of loyalty points the user currently has available
user.goldTotal                    number   Number of loyalty points the user has earned all time
user.goldSpent                    number   Number of loyalty points the user has spent
user.id                           number   The ID of the user
user.ssoId                        [string] The SSO identifier of the user
user.loyaltyMembership            [object] The membership the user is subscribed to
user.loyaltyMembership.id         number   The ID of the membership
user.loyaltyMembership.name       string   The name of the membership
user.loyaltyMembership.priceMonth number   The cost of the membership per month in cents
user.loyaltyMembership.priceYear  number   The cost of the membership per year in cents
user.loyaltyMembership.resourceId number   The resource ID of the membership badge icon
user.loyaltyTier                  [object] The tier the user is subscribed to
user.loyaltyTier.id               number   The ID of the tier
user.loyaltyTier.name             string   The name of the tier
user.loyaltyTier.gold             number   The points required to achieve tier
user.loyaltyTier.resourceId       number   The resource ID of the tier badge icon
user.name                         string   The name of the user
user.notifications                string   The last time the user read the notifications formatted as ISO date string
user.shippingAddressCity          string   Shipping info for the user
user.shippingAddressCountry       string   Shipping info for the user
user.shippingAddressName          string   Shipping info for the user
user.shippingAddressState         string   Shipping info for the user
user.shippingAddressStreet        string   Shipping info for the user
user.shippingAddressSuite         string   Shipping info for the user
user.shippingAddressZip           string   Shipping info for the user
user.tags                         object[] List of tags the user is interested in
user.tags.id                      number   The ID of the tag
user.tags.name                    string   The name of the tag
================================= ======== =================================================================================

Add Points
----------

Add points to a user

- **POST** /user/:id/points

Request

=========== ======== =============================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================
points      number   The amount of points to add to the user
message     string   The message to log with the transaction
key         [string] If included, transactions will be limited to one key per user (this will prevent duplicate point assignments)
=========== ======== =============================================================================================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/admin/user/1/points', {
      points: 100,
      message: 'Watched VOD content',
      key: '12345xyz',
   }, {
      headers: {
         'client-id': 'xxxxx-xxxxx-xxxxx-xxxxx',
      },
   });

Response

================================== ======== =================================================================================
Field                              Type     Description
================================== ======== =================================================================================
success                            boolean  always true
================================== ======== =================================================================================

Delete User
-----------

Delete a user

- **DELETE** /user/:id

Request

.. code-block:: js

   const response = await axios.delete('https://botisimo.com/api/v1/loyalty/admin/user/1', {
      headers: {
         'client-id': 'xxxxx-xxxxx-xxxxx-xxxxx',
      },
   });

Response

================================== ======== =================================================================================
Field                              Type     Description
================================== ======== =================================================================================
success                            boolean  always true
================================== ======== =================================================================================
