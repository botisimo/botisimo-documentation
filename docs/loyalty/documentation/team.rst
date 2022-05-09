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

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team');

Response

======================================= ======== =======================================
Field                                   Type     Description
======================================= ======== =======================================
team                                    object
team.name                               string   The name of the team
team.currencyName                       string   The name of the loyalty points
team.loyaltyMemberships                 object[] List of memberships
team.loyaltyMemberships.id              number   The ID of the membership
team.loyaltyMemberships.name            string   The name of the membership
team.loyaltyMemberships.description     string   The membership description
team.loyaltyMemberships.priceMonth      number   The cost of the membership per month in cents
team.loyaltyMemberships.priceYear       number   The cost of the membership per year in cents
team.loyaltyMemberships.goldMultiplier  number   The loyalty points multiplier for this membership
team.loyaltyMemberships.resourceId      number   The resource ID of the membership image
team.loyaltyMemberships.badgeResourceId number   The resource ID of the membership badge
team.loyaltyTiers                       object[] List of tiers
team.loyaltyTiers.id                    number   The ID of the tier
team.loyaltyTiers.name                  string   The name of the tier
team.loyaltyTiers.description           string   The tier description
team.loyaltyTiers.gold                  number   The points required to achieve tier
team.loyaltyTiers.resourceId            number   The resource ID of the tier image
team.loyaltyTiers.badgeResourceId       number   The resource ID of the tier badge
team.tags                               object[] List of tags
team.tags.id                            number   The ID of the tag
team.tags.name                          string   The name of the tag
======================================= ======== =======================================

Example

.. code-block:: js

   {
      "team": {
         "name": "OpTic Gaming",
         "currencyName": "Points",
         "loyaltyMemberships": [
               {
                  "id": 4,
                  "enabled": true,
                  "archived": false,
                  "order": 0,
                  "name": "Gold",
                  "description": "Stay connected with your favorite teams, players, and creators at OpTic!",
                  "priceMonth": 500,
                  "priceYear": 3000,
                  "goldMultiplier": 1,
                  "resourceId": 6812,
                  "badgeResourceId": null,
                  "createdAt": "2022-03-07T22:58:17.000Z",
                  "updatedAt": "2022-03-19T15:25:25.000Z"
               },
               ...
         ],
         "loyaltyTiers": [
               {
                  "id": 4,
                  "enabled": true,
                  "archived": false,
                  "order": 0,
                  "name": "Prestige 1",
                  "description": "Stay connected with your favorite teams, players, and creators at OpTic!",
                  "gold": 10000000,
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
