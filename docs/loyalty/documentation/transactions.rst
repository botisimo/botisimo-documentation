Transactions API
================

- `List Transactions`_

List Transactions
-----------------

List transactions

- **GET** /transaction/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/transaction/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

========================= ======== =======================================
Field                     Type     Description
========================= ======== =======================================
transactions              object[]
transactions.id           number   The ID of the transaction
transactions.amount       number   The amount of points for the transaction (may be positive or negative)
transactions.createdAt    string   The ISO date of when the transaction was created
transactions.description  string   The transaction display text
transactions.mission      [object] The mission connected to the transaction, if one exists
transactions.rpgShopItem  [object] The shop item connected to the transaction, if one exists
transactions.link         [string] The URL link related to the transaction, if one exists
========================= ======== =======================================
