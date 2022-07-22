Notifications API
=================

- `List Notifications`_

List Notifications
------------------

List notifications

- **GET** /notification/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/notification/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

========================== ======== =======================================
Field                      Type     Description
========================== ======== =======================================
notifications              object[]
notifications.id           number   The ID of the notification
notifications.timestamp    string   The ISO date of when the notification was created
notifications.body         string   The notification display text
notifications.event        [object] The event connected to the notification, if one exists
notifications.mission      [object] The mission connected to the notification, if one exists
notifications.rpgShopItem  [object] The shop item connected to the notification, if one exists
notifications.resourceId   [number]   The resource ID of the notification image. You should use the resource ID from the ``event``, ``mission``, or ``rpgShopItem`` if they exist
notifications.link         [string] The URL link related to the notification, if one exists
========================== ======== =======================================
