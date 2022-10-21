User API Documentation
======================

- `API Endpoint`_
- `Errors`_
- :doc:`Team API <team>`
- :doc:`Authentication API <authentication>`
- :doc:`User API <user>`
- :doc:`Billing API <billing>`
- :doc:`Memberships API <memberships>`
- :doc:`Tiers API <tiers>`
- :doc:`Creators API <creators>`
- :doc:`Missions API <missions>`
- :doc:`Shop Items API <shopItems>`
- :doc:`Events API <events>`
- :doc:`Transactions API <transactions>`
- :doc:`Notifications API <notifications>`
- :doc:`Gifts API <gifts>`

.. toctree::
   :maxdepth: 1
   :name: toc-loyalty-user-documentation
   :hidden:

   team
   authentication
   user
   billing
   memberships
   tiers
   creators
   missions
   shopItems
   events
   transactions
   notifications
   gifts

API Endpoint
------------

The API is located at the following URL. You should replace ``:team`` with your team's name in your Botisimo account::

   https://botisimo.com/api/v1/loyalty/:team

Authenticating Requests
-----------------------

Authenticated requests should include the ``token`` received from :doc:`Authentication API <authentication>` as a header on the request ``x-user-auth-token``

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/mission/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Fetching Media Resources
------------------------

Some objects have a ``resourceId`` that correlates to a media file in S3. You can fetch any resource by using the ``resourceId``::

   https://s3.amazonaws.com/prod.botisimo.com/resource/:resourceId

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
