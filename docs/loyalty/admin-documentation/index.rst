Admin API Documentation
=======================

- `API Endpoint`_
- `Errors`_
- :doc:`User API <user>`

.. toctree::
   :maxdepth: 1
   :name: toc-loyalty-admin-documentation
   :hidden:

   user

API Endpoint
------------

The API is located at the following URL::

   https://botisimo.com/api/v1/loyalty/admin

Authenticating Requests
-----------------------

Authenticated requests should include a ``Client ID`` generated from your Botisimo account `profile <https://botisimo.com/account/profile>`_ as a header on the request ``client-id``

.. code-block:: js

   const response = await axios.post('https://botisimo.com/api/v1/loyalty/admin/user/1/points', { ... }, {
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
