Billing API
===========

- `Upgrade Tier`_
- `Confirm Upgrade Tier`_
- `Manage Billing`_

Upgrade Tier
------------

The upgrade request should be made first when updating a subscription.
If the new tier is a free subscription, then the update will be processed immediately.
If the new tier is a paid subscription, then it will return information about the upgrade to be confirmed by the user. If confirmation is required, then the client should ask the user to confirm and then use the ``/billing/confirm`` endpoint.

- **GET** /billing/upgrade

Request

=========== ======== =====================================================
Field       Type     Description
=========== ======== =====================================================
interval    string   The billing interval. Should be ``month`` or ``year``
tier        number   Tier ID
=========== ======== =====================================================

Response

=========== ======== =============================================================================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================================================================
amountDue   [number] The amount due in cents to process the upgrade. If included, the user should be prompted to confirm the amount and then use the ``/billing/confirm`` endpoint
href        [string] If included, you should immediately redirect to this href
=========== ======== =============================================================================================================================================================

Confirm Upgrade Tier
--------------------

This endpoint should ONLY be used after first using the ``/billing/upgrade`` endpoint and prompting the user to confirm the transaction.

- **GET** /billing/confirm

Request

=========== ======== =====================================================
Field       Type     Description
=========== ======== =====================================================
interval    string   The billing interval. Should be ``month`` or ``year``
tier        number   Tier ID
=========== ======== =====================================================

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

Response

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
href        string   The href to the billing management session
=========== ======== ==========================================
