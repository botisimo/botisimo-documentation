User API
========

- `Add Points`_

Add Points
----------

Add points to a user

- **POST** /user/:id/points

Request

=========== ======== =============================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================
points      number   The amount of points to add to the user
message     string   The message to log with the transaction
key         [string] If included, transactions will be limited to one key per user (this will prevent duplicate point assignments)
=========== ======== =============================================================================================================

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/admin/user/1/points', {
      points: 100,
      message: 'Watched VOD content',
      key: '12345xyz',
   }, {
      headers: {
         'client-id': 'xxxxx-xxxxx-xxxxx-xxxxx',
      },
   });

Response

================================== ======== =================================================================================
Field                              Type     Description
================================== ======== =================================================================================
success                            boolean  always true
================================== ======== =================================================================================
