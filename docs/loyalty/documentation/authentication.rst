Authentication API
==================

- `Sign Up`_
- `Log In`_
- `Initiate OAuth Flow`_
- `Get User`_

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
tier        number   Tier ID
=========== ======== ======================================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/:team/login', {
      email: 'xxxxx',
      password: 'xxxxx',
      interval: 'month',
      dateOfBirth: '12/25/1990',
      tier: 1,
      tags: [1, 2, 3, 4],
   });

Response

=========================== ======== =================================================================================
Field                       Type     Description
=========================== ======== =================================================================================
href                        [string] If included, you should store the ``token`` and immediately redirect to this href
token                       string   Token for future requests that require authentication
user                        object   Information about the logged in user
user.avatar                 string   URL to to user avatar
user.createdAt              string   When the user was created
user.dateOfBirth            string   Date of birth formatted as ``MM/DD/YYYY``
user.gold                   number   Number of loyalty points the user currently has available
user.goldTotal              number   Number of loyalty points the user has earned all time
user.goldSpent              number   Number of loyalty points the user has spent
user.id                     number   The ID of the user
user.loyaltyTier            object   The tier the user is subscribed to
user.loyaltyTier.id         number   The ID of the tier
user.loyaltyTier.name       string   The name of the tier
user.loyaltyTier.priceMonth number   The cost of the tier per month in cents
user.loyaltyTier.priceYear  number   The cost of the tier per year in cents
user.loyaltyTier.resourceId number   The resource ID of the tier badge icon
user.name                   string   The name of the user
user.notifications          string   The last time the user read the notifications formatted as ISO date string
user.shippingAddressCity    string   Shipping info for the user
user.shippingAddressCountry string   Shipping info for the user
user.shippingAddressName    string   Shipping info for the user
user.shippingAddressState   string   Shipping info for the user
user.shippingAddressStreet  string   Shipping info for the user
user.shippingAddressSuite   string   Shipping info for the user
user.shippingAddressZip     string   Shipping info for the user
user.tags                   object[] List of tags the user is interested in
user.tags.id                number   The ID of the tag
user.tags.name              string   The name of the tag
=========================== ======== =================================================================================

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

=========================== ======== ==========================================================================
Field                       Type     Description
=========================== ======== ==========================================================================
token                       string   Token for future requests that require authentication
user                        object   Information about the logged in user
user.avatar                 string   URL to to user avatar
user.createdAt              string   When the user was created
user.dateOfBirth            string   Date of birth formatted as ``MM/DD/YYYY``
user.gold                   number   Number of loyalty points the user currently has available
user.goldTotal              number   Number of loyalty points the user has earned all time
user.goldSpent              number   Number of loyalty points the user has spent
user.id                     number   The ID of the user
user.loyaltyTier            object   The tier the user is subscribed to
user.loyaltyTier.id         number   The ID of the tier
user.loyaltyTier.name       string   The name of the tier
user.loyaltyTier.priceMonth number   The cost of the tier per month in cents
user.loyaltyTier.priceYear  number   The cost of the tier per year in cents
user.loyaltyTier.resourceId number   The resource ID of the tier badge icon
user.name                   string   The name of the user
user.notifications          string   The last time the user read the notifications formatted as ISO date string
user.shippingAddressCity    string   Shipping info for the user
user.shippingAddressCountry string   Shipping info for the user
user.shippingAddressName    string   Shipping info for the user
user.shippingAddressState   string   Shipping info for the user
user.shippingAddressStreet  string   Shipping info for the user
user.shippingAddressSuite   string   Shipping info for the user
user.shippingAddressZip     string   Shipping info for the user
user.tags                   object[] List of tags the user is interested in
user.tags.id                number   The ID of the tag
user.tags.name              string   The name of the tag
=========================== ======== ==========================================================================

Initiate OAuth Flow
-------------------

To initiate an OAuth request, you should redirect the user to this URL. You should replace ``:team`` with your team's name in your Botisimo account. You should replace ``:platform`` with the platform you want to use.

Platform can be: ``twitch``, ``youtube``, ``facebook``, ``instagram``, ``discord``, ``twitter``, ``spotify``, ``steam``, ``battlenet``, ``chess``, ``tiktok``

- **GET** https://botisimo.com/api/v1/auth/:platform/user/loyalty/:team
- **GET** https://botisimo.com/api/v1/auth/:platform/user/loyalty/:team?user_auth_token=xxxxxx

Request

=============== ======== ============================================================================================
Field           Type     Description
=============== ======== ============================================================================================
user_auth_token [string] If the user is already logged in, you should include the authentication ``token`` in the URL
=============== ======== ============================================================================================

Get User
--------

- **GET** /user

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
email       string
password    string
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/user', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=========================== ======== ==========================================================================
Field                       Type     Description
=========================== ======== ==========================================================================
unread                      number   Number of unread notifications for this user
user                        object   Information about the logged in user
user.avatar                 string   URL to to user avatar
user.createdAt              string   When the user was created
user.dateOfBirth            string   Date of birth formatted as ``MM/DD/YYYY``
user.gold                   number   Number of loyalty points the user currently has available
user.goldTotal              number   Number of loyalty points the user has earned all time
user.goldSpent              number   Number of loyalty points the user has spent
user.id                     number   The ID of the user
user.loyaltyTier            object   The tier the user is subscribed to
user.loyaltyTier.id         number   The ID of the tier
user.loyaltyTier.name       string   The name of the tier
user.loyaltyTier.priceMonth number   The cost of the tier per month in cents
user.loyaltyTier.priceYear  number   The cost of the tier per year in cents
user.loyaltyTier.resourceId number   The resource ID of the tier badge icon
user.name                   string   The name of the user
user.notifications          string   The last time the user read the notifications formatted as ISO date string
user.shippingAddressCity    string   Shipping info for the user
user.shippingAddressCountry string   Shipping info for the user
user.shippingAddressName    string   Shipping info for the user
user.shippingAddressState   string   Shipping info for the user
user.shippingAddressStreet  string   Shipping info for the user
user.shippingAddressSuite   string   Shipping info for the user
user.shippingAddressZip     string   Shipping info for the user
user.tags                   object[] List of tags the user is interested in
user.tags.id                number   The ID of the tag
user.tags.name              string   The name of the tag
=========================== ======== ==========================================================================

Example

.. code-block:: js

    {
        "unread": 0,
        "user": {
            "id": 30758,
            "createdAt": "2021-07-12T21:15:53.000Z",
            "updatedAt": "2022-04-08T17:05:55.000Z",
            "emailUser": {
                "id": 1239,
                "email": "oscar@otothea.com",
                "name": "oscar@otothea.com",
                "displayName": "Oscar",
                "createdAt": "2021-07-12T02:00:00.000Z"
            },
            "twitchUser": {
                "id": 2,
                "twitchId": 87416554,
                "name": "otothea",
                "chatName": "otothea",
                "displayName": "OtotheA",
                "createdAt": "2017-02-25T02:31:31.000Z"
            },
            "youtubeUser": {
                "id": 129076,
                "youtubeChannelId": "UCjX4fLpD7BNtYwuLEl2xwPg",
                "name": "botisimo",
                "displayName": "Botisimo",
                "createdAt": "2018-06-29T04:47:32.000Z"
            },
            "facebookUser": {
                "id": 29,
                "facebookId": "2148122302184574",
                "name": "Luna Doge",
                "displayName": "Luna Doge",
                "createdAt": "2020-06-22T20:38:48.000Z"
            },
            "twitterUser": {
                "id": 1,
                "twitterId": "835748192708923392",
                "name": "Botisimo",
                "displayName": "Botisimo",
                "createdAt": "2021-03-24T01:56:45.000Z"
            },
            "discordUser": {
                "id": 1,
                "discordId": "187951925965225984",
                "name": "OtotheA",
                "displayName": "OtotheA",
                "createdAt": "2017-02-24T23:07:04.000Z"
            },
            "spotifyUser": {
                "id": 1,
                "spotifyId": "1221486274",
                "name": "1221486274",
                "displayName": "Chip Armstrong",
                "createdAt": "2021-04-06T22:35:06.000Z"
            },
            "steamUser": {
                "id": 1,
                "steamId": "76561197978302905",
                "name": "OtotheA",
                "displayName": "Oscar",
                "createdAt": "2022-02-25T20:54:39.000Z"
            },
            "tiktokUser": {
                "id": 1,
                "tiktokId": "76561197978302905",
                "name": "OtotheA",
                "displayName": "Oscar",
                "createdAt": "2022-02-25T20:54:39.000Z"
            },
            "name": "otothea",
            "avatar": "https://static-cdn.jtvnw.net/jtv_user_pictures/974caf6e-4ad3-4d42-a495-7e73280a2c36-profile_image-300x300.png",
            "notifications": "2022-04-08T16:53:36.000Z",
            "loyaltyTier": {
                "id": 4,
                "enabled": true,
                "order": 0,
                "name": "Silver",
                "description": "Stay connected with your favorite teams, players, and creators at OpTic!",
                "priceMonth": 0,
                "priceYear": 0,
                "gold": 0,
                "goldMultiplier": 1,
                "stripeProductId": "prod_xxxxx",
                "stripeMonthlyPlanId": "plan_xxxxx
                "stripeYearlyPlanId": "plan_xxxxx",
                "stripePointsPlanId": "price_xxxxx",
                "resourceId": 6812,
                "badgeResourceId": null,
                "createdAt": "2022-03-07T22:58:17.000Z",
                "updatedAt": "2022-03-19T15:25:25.000Z"
            },
            "dateOfBirth": "06/25/1988",
            "shippingAddressName": null,
            "shippingAddressStreet": null,
            "shippingAddressSuite": null,
            "shippingAddressCity": null,
            "shippingAddressState": null,
            "shippingAddressZip": null,
            "shippingAddressCountry": null,
            "tags": [
                {
                    "id": 3,
                    "name": "OpTic Texas",
                    "createdAt": "2022-03-07T23:15:50.000Z"
                },
                {
                    "id": 9,
                    "name": "Scump",
                    "createdAt": "2022-03-08T21:40:08.000Z"
                }

                ...
            ],
            "gold": 2519385,
            "goldSpent": 10040000,
            "goldTotal": 12559385
        }
    }
