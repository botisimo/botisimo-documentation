API Documentation
=================

- `API Endpoint`_
- `Errors`_
- :doc:`Team API <team>`
- :doc:`Authentication API <authentication>`
- :doc:`Billing API <billing>`
- :doc:`Tiers API <tiers>`
- :doc:`Missions API <missions>`
- :doc:`Shop Items API <shopItems>`
- :doc:`Events API <events>`

.. toctree::
   :maxdepth: 1
   :name: toc-loyalty-documentation
   :hidden:

   team
   authentication
   billing
   tiers
   shopItems
   missions
   events

API Endpoint
------------

The API is located at the following URL. You should replace ``:team`` with your team's name in your Botisimo account

``https://botisimo.com/api/v1/loyalty/:team``

Errors
------

Any errors will be returned with a non-2XX status code.

Response

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
message     string   The message describing the error
=========== ======== ==========================================
