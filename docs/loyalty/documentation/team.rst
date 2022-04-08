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

Example

.. code-block:: json

    {
        "team": {
            "name": "OpTic Gaming",
            "currencyName": "Points",
            "loyaltyTiers": [
                {
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
                ...
            ],
            "tags": [
                {
                    "id": 3,
                    "name": "OpTic Texas",
                    "createdAt": "2022-03-07T23:15:50.000Z"
                },
                {
                    "id": 4,
                    "name": "OpTic Gaming",
                    "createdAt": "2022-03-07T23:16:12.000Z"
                },
                {
                    "id": 5,
                    "name": "H3CZ",
                    "createdAt": "2022-03-07T23:16:28.000Z"
                },
                {
                    "id": 6,
                    "name": "Hitch",
                    "createdAt": "2022-03-08T21:37:51.000Z"
                },
                ...
            ],
        }
    }
