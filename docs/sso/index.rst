Single Sign On
==============

Generate Single Sign On (SSO) links to allow your users to log in to botisimo with your service. Must have an enterprise team account on Botisimo.

- `API Endpoint`_
- `Errors`_
- `Get Link`_

API Endpoint
------------

The API is located at the following URL::

   https://botisimo.com/api/v1/guild

Authenticating Requests
-----------------------

Authenticated requests should include a ``Client ID`` generated from your Botisimo account `profile <https://botisimo.com/account/profile>`_ as a header on the request ``client-id``

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/guild/sso?email=joe.someone@example.com&id=1234567890', {
      headers: {
         'client-id': 'xxxxx-xxxxx-xxxxx-xxxxx',
      },
   });

Errors
------

Any errors will be returned with a non-2XX status code.

Response

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
message     string   The message describing the error
=========== ======== ==========================================

Example

.. code-block:: js

   {
      message: "An error has occurred"
   }

Get Link
--------

Get or create a link to login to account

- **GET** /sso

Request

=========== ======== =============================================================================================================
Field       Type     Description
=========== ======== =============================================================================================================
id          string   The SSO identifier of the account, usually an internal ID from your system
email       string   The email address of the account
=========== ======== =============================================================================================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/guild/sso', {
      params: {
         id: '1234567890',
         email: 'joe.someone@example.com',
      },
      headers: {
         'client-id': 'xxxxx-xxxxx-xxxxx-xxxxx',
      },
   });

Response

=========== ======== =================================================================================
Field       Type     Description
=========== ======== =================================================================================
href        string   Link to redirect the users to log in to Botisimo account
=========== ======== =================================================================================
