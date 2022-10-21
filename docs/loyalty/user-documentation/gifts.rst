User API
========

- `Send Gift`_
- `Verify Gift Token`_

Send Gift
---------

After initiating a the gift flow, you will be given a URL for the checkout session.

After checkout, an email will be sent to the recipient's inbox. The email will have a link with a token in it. Your client should be able to handle this token when the user clicks on the link. The link looks like this::

   https://yourapp.com/?gift_token=xxxxx

When the user lands on this page, you should submit the token to the ``/gift/verify`` endpoint to get info about the gift

- **POST** /gift

Request

====================== ========== ==========================================================================
Field                  Type       Description
====================== ========== ==========================================================================
membershipId           string     ID of the membership to gift
senderEmail            string     Email address of the sender
recipientEmail         string     Email address of the gift recipient
returnPath             [string]   The URL path to return to after stripe checkout
====================== ========== ==========================================================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/:team/gift', {
      membershipId: 2,
      senderEmail: 'jack@example.com',
      recipientEmail: 'jill@example.com',
      returnPath: '/gift?completed=true',
   }, {
      headers: {
         'x-user-auth-token': 'xxxxxxx', // In this case the auth token is optional
      },
   });

Response

=========== ======== =====================================================================================
Field       Type     Description
=========== ======== =====================================================================================
href        string   The href to the Stripe checkout session, you should immediately redirect to this href
=========== ======== =====================================================================================

.. code-block:: js

   {
      "href": "https://xxxxx"
   }

Verify Gift Token
-----------------

This endpoint should ONLY be used if you have a token from a ``/gift`` request

- **POST** /gift/verify

Request

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
token       string   The token from the gift
=========== ======== ======================================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/:team/gift/verify', {
      token: 'xxxxx'
   });

Response

====================================== ======== =================================================================================
Field                                  Type     Description
====================================== ======== =================================================================================
gift                                   object
gift.email                             string   The email address of the gift recipient
gift.loyaltyMembership                 object
gift.loyaltyMembership.id              number   The ID of the membership
gift.loyaltyMembership.name            string   The name of the membership
gift.loyaltyMembership.description     string   The membership description
gift.loyaltyMembership.priceMonth      number   The cost of the membership per month in cents
gift.loyaltyMembership.priceYear       number   The cost of the membership per year in cents
gift.loyaltyMembership.gold            number   The price in loyalty points to redeem
gift.loyaltyMembership.goldMultiplier  number   The loyalty points multiplier for this membership
gift.loyaltyMembership.resourceId      number   The resource ID of the membership image
gift.loyaltyMembership.badgeResourceId number   The resource ID of the membership badge
====================================== ======== =================================================================================
