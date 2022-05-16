Authentication API
==================

- `Sign Up`_
- `Log In`_
- `Initiate OAuth Flow`_

Sign Up
-------

- **POST** /signup

Request

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
dateOfBirth string   Date of birth. Should be formatted like ``MM/DD/YYYY``
email       string   Email address used to identify and communicate with
interval    string   The billing interval. Should be ``month`` or ``year``
password    string
tags        number[] Array of Tag IDs
membership  number   Membership ID
=========== ======== ======================================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/:team/login', {
      email: 'xxxxx',
      password: 'xxxxx',
      interval: 'month',
      dateOfBirth: '12/25/1990',
      membership: 1,
      tags: [1, 2, 3, 4],
   });

Response

================================= ======== =================================================================================
Field                             Type     Description
================================= ======== =================================================================================
href                              [string] If included, you should store the ``token`` and immediately redirect to this href
token                             string   Token for future requests that require authentication
user                              object   Information about the logged in user
user.avatar                       string   URL to to user avatar
user.createdAt                    string   When the user was created
user.dateOfBirth                  string   Date of birth formatted as ``MM/DD/YYYY``
user.gold                         number   Number of loyalty points the user currently has available
user.goldTotal                    number   Number of loyalty points the user has earned all time
user.goldSpent                    number   Number of loyalty points the user has spent
user.id                           number   The ID of the user
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

Log In
------

- **POST** /login

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
email       string
password    string
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/:team/login', {
      email: 'xxxxx',
      password: 'xxxxx',
   });

Response

================================= ======== ==========================================================================
Field                             Type     Description
================================= ======== ==========================================================================
token                             string   Token for future requests that require authentication
user                              object   Information about the logged in user
user.avatar                       string   URL to to user avatar
user.createdAt                    string   When the user was created
user.dateOfBirth                  string   Date of birth formatted as ``MM/DD/YYYY``
user.gold                         number   Number of loyalty points the user currently has available
user.goldTotal                    number   Number of loyalty points the user has earned all time
user.goldSpent                    number   Number of loyalty points the user has spent
user.id                           number   The ID of the user
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
================================= ======== ==========================================================================

Initiate OAuth Flow
-------------------

To initiate an OAuth request, you should redirect the user to this URL. You should replace ``:team`` with your team's name in your Botisimo account. You should replace ``:platform`` with the platform you want to use. If the user is already logged in and you want to connect to the same account, you should include the ``user_auth_token`` in the URL. If you do not include the ``user_auth_token`` in the URL then it will attempt to make a new account.

Platform can be: ``twitch``, ``youtube``, ``facebook``, ``instagram``, ``discord``, ``twitter``, ``spotify``, ``steam``, ``battlenet``, ``chess``, ``tiktok``

- **GET** https\://botisimo.com/api/v1/auth/:platform/user/loyalty/:team
- **GET** https\://botisimo.com/api/v1/auth/:platform/user/loyalty/:team?user_auth_token=xxxxxx

Request

=============== ======== ============================================================================================
Field           Type     Description
=============== ======== ============================================================================================
user_auth_token [string] If the user is already logged in, you should include the authentication ``token`` in the URL
=============== ======== ============================================================================================
