GraphQL API
===========

Welcome to the Botisimo GraphQL API. If you are new to GraphQL you can learn more about it here `https://graphql.org/learn <https://graphql.org/learn>`_.

.. toctree::
   :maxdepth: 1
   :name: toc-extras-graphql
   :caption: Additional Resources

   Reference <https://botisimo.com/docs/graphql/reference/>
   Playground <https://botisimo.com/graphql/playground>

GraphQL Endpoint
^^^^^^^^^^^^^^^^

The Botisimo GraphQL API endpoint is located at::

    https://botisimo.com/graphql

Authentication
^^^^^^^^^^^^^^

The Botisimo GraphQL API requires a Client ID to make authenticated requests. You can obtain your Client ID by visiting your `account settings <https://botisimo.com/account/settings>`_ and copying the Client ID found in the "Developer" section. Keep this Client ID a secret because anyone who has it has access to your account.

This Client ID will need to be included as a ``Client-ID`` header in all GraphQL requests.

Query the API
^^^^^^^^^^^^^

You can access the Botisimo GraphQL API endpoint using `cURL <https://curl.haxx.se/>`_ or any other HTTP client. For the following example, make sure to replace **<CLIENT_ID>** with the Client ID you copied from your `account settings <https://botisimo.com/account/settings>`_.

> cURL
------

To make a query to the Botisimo GraphQL API using `cURL <https://curl.haxx.se/>`_, send a POST request with your query as the payload::

    curl -X POST "https://botisimo.com/graphql" \
    -H "Content-Type: application/graphql" \
    -H "Client-ID: <CLIENT_ID>" \
    -d '
    query {
      account {
        id
        email
        createdAt
      }
    }'

Examples
^^^^^^^^

Here's how you might fetch the Twitch connections on your account and then add currency to a user on one of the Twitch connections

> Fetch Twitch Connection IDs
-----------------------------

request::

    query {
      twitchConnections(pagination: {limit: 1}) {
        edges {
          node {
            id
            twitchName
          }
        }
      }
    }

response::

    {
      "data": {
        "twitchConnections": {
          "edges": [
            {
              "node": {
                "id": 1,
                "twitchName": "botisimo"
              }
            }
          ]
        }
      },
    }

> Fetch Twitch Connection Users
-------------------------------

request::

    query {
      twitchConnectionUsers(twitchConnectionId: 1, pagination: {limit: 1}) {
        edges {
          node {
            id
            currency
            twitchUser {
              name
            }
          }
        }
      }
    }

response::

    {
      "data": {
        "twitchConnectionUsers": {
          "edges": [
            {
              "node": {
                "id": 1,
                "currency": 1400,
                "twitchUser": {
                  "name": "otothea"
                }
              }
            }
          ]
        }
      }
    }

> Add Currency to a Twitch Connection User
------------------------------------------

request::

    mutation {
      addCurrency(
        platform: TWITCH,
        id: "otothea",
        amount: 100,
        connectionId: 1
      ) {
        ... on TwitchConnectionUser {
          id
          currency
          twitchUser {
            name
          }
        }
      }
    }

response::

    {
      "data": {
        "addCurrency": {
          "id": 1,
          "currency": 1500,
          "twitchUser": {
            "name": "otothea"
          }
        }
      }
    }
