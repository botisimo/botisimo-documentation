Team API
========

- `Read Team`_

Read Team
---------

Get the information about the team

- **GET** /

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

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
