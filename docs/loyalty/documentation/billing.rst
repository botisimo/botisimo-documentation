Billing API
===========

- `Update Membership`_
- `Confirm Update Membership`_
- `Manage Billing`_

Update Membership
-----------------

The update request should be made first when updating a subscription.
If the new membership is a free subscription, then the update will be processed immediately.
If the new membership is a paid subscription, then it will return information about the update to be confirmed by the user. If confirmation is required, then the client should ask the user to confirm and then use the ``/billing/confirm`` endpoint.

- **GET** /billing/update

Request

=========== ======== =====================================================
Field       Type     Description
=========== ======== =====================================================
interval    string   The billing interval. Should be ``month`` or ``year``
membership  number   Membership ID
=========== ======== =====================================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/billing/update', {
      params: {
         interval: 'month',
         membership: 1
      },
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=========== ======== =============================================================================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================================================================
amountDue   [number] The amount due in cents to process the update. If included, the user should be prompted to confirm the amount and then use the ``/billing/confirm`` endpoint
href        [string] If included, you should immediately redirect to this href
=========== ======== =============================================================================================================================================================

.. code-block:: js

   {
      "amountDue": 4999
   }

Confirm Update Membership
-------------------------

This endpoint should ONLY be used after first using the ``/billing/update`` endpoint and prompting the user to confirm the transaction.

- **GET** /billing/confirm

Request

=========== ======== =====================================================
Field       Type     Description
=========== ======== =====================================================
interval    string   The billing interval. Should be ``month`` or ``year``
membership  number   Membership ID
=========== ======== =====================================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/billing/confirm', {
      params: {
         interval: 'month',
         membership: 1
      },
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=========== ======== =============================================================================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================================================================
href        [string] If included, you should redirect to this href for adding a card
=========== ======== =============================================================================================================================================================

Manage Billing
--------------

Use this endpoint to request a URL for a billing management portal session

- **GET** /billing/manage

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/billing/manage', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
href        string   The href to the billing management session
=========== ======== ==========================================

.. code-block:: js

   {
      "href": "https://xxxxx"
   }
