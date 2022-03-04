=========================
Loyalty API Documentation
=========================

- `API Endpoint`_
- `Get Team Info`_
- `Sign Up`_
- `Log In`_
- `Upgrade Tier`_
- `Confirm Upgrade Tier`_
- `Manage Billing`_

API Endpoint
============

The API is located at the following URL. You should replace ``:team`` with your team's name in your Botisimo account

``https://botisimo.com/api/v1/loyalty/:team``

Get Team Info
-------------

Get the information about the team

- **GET** /

Request

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
\-          \-       \-
=========== ======== ======================================================

Response

============================ ======== =======================================
Field                        Type     Description
============================ ======== =======================================
team                         object
team.name                    string   The name of the team
team.currencyName            string   The name of the loyalty points
team.loyaltyTiers            object[] List of tiers
team.loyaltyTiers.id         number   The ID of the tier
team.loyaltyTiers.name       string   The name of the tier
team.loyaltyTiers.priceMonth number   The cost of the tier per month in cents
team.loyaltyTiers.priceYear  number   The cost of the tier per year in cents
team.loyaltyTiers.resourceId number   The resource ID of the tier badge icon
team.tags                    object[] List of tags
team.tags.id                 number   The ID of the tag
team.tags.name               string   The name of the tag
============================ ======== =======================================

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

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
email       string
password    string
=========== ======== ======================================================

Response

=========================== ======== ==========================================================================
Field                       Type     Description
=========================== ======== ==========================================================================
token                       string   Token for future requests that require authentication
user                        object   Information about the logged in user
user                        object   Information about the logged in user
user.avatar                 string   URL to to user avatar
user.createdAt              string   When the user was created
user.dateOfBirth            string   Date of birth formatted as ``MM/DD/YYYY``
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

Upgrade Tier
------------

The upgrade request should be made first when updating a subscription.
If the new tier is a free subscription, then the update will be processed immediately.
If the new tier is a paid subscription, then it will return information about the upgrade to be confirmed by the user. If confirmation is required, then the client should ask the user to confirm and then use the ``/billing/confirm`` endpoint.

- **GET** /billing/upgrade

Request

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
interval    string   The billing interval. Should be ``month`` or ``year``
tier        number   Tier ID
=========== ======== ======================================================

Confirm Upgrade Tier
--------------------

This endpoint should ONLY be used after first using the ``/billing/upgrade`` endpoint and prompting the user to confirm the transaction.

- **GET** /billing/confirm

Request

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
interval    string   The billing interval. Should be ``month`` or ``year``
tier        number   Tier ID
=========== ======== ======================================================

Manage Billing
--------------

Use this endpoint to request a URL for a billing management portal session

- **GET** /billing/manage

Request

=========== ======== ======================================================
Field       Type     Description
=========== ======== ======================================================
\-          \-       \-
=========== ======== ======================================================
