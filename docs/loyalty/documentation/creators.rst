Creators API
============

- `List Creators`_

List Creators
-------------

List creators

- **GET** /creator/list

Request

=========== ======== ==========================================
Field       Type     Description
=========== ======== ==========================================
\-          \-       \-
=========== ======== ==========================================

.. code-block:: js

   const response = await axios.get('https://botisimo.com/api/v1/loyalty/:team/creator/list', {
      headers: {
         'x-user-auth-token': 'xxxxxxx',
      },
   });

Response

================================================ ======== =======================================
Field                                            Type     Description
================================================ ======== =======================================
creators                                         object[]
creators.id                                      number   The ID of the creator
creators.hasTwitch                               boolean
creators.twitchConnections                       object[]
creators.twitchConnections.twitchId              string
creators.twitchConnections.twitchLogo            string
creators.twitchConnections.twitchDisplayName     string
creators.twitchConnections.enabled               boolean
creators.twitchConnections.online                boolean
creators.twitchConnections.currentViewers        number
creators.hasYoutube                              boolean
creators.youtubeConnections                      object[]
creators.youtubeConnections.youtubeId            string
creators.youtubeConnections.youtubeLogo          string
creators.youtubeConnections.youtubeDisplayName   string
creators.youtubeConnections.enabled              boolean
creators.youtubeConnections.online               boolean
creators.youtubeConnections.currentViewers       number
creators.hasFacebook                             boolean
creators.facebookConnections                     object[]
creators.facebookConnections.facebookId          string
creators.facebookConnections.facebookLogo        string
creators.facebookConnections.facebookDisplayName string
creators.facebookConnections.enabled             boolean
creators.facebookConnections.online              boolean
creators.facebookConnections.currentViewers      number
creators.hasTwitter                              boolean
creators.twitterConnections                      object[]
creators.twitterConnections.twitterId            string
creators.twitterConnections.twitterLogo          string
creators.twitterConnections.twitterDisplayName   string
creators.twitterConnections.enabled              boolean
creators.twitterConnections.online               boolean
creators.twitterConnections.currentViewers       number
creators.live                                    boolean
creators.logo                                    string
================================================ ======== =======================================

Example

.. code-block:: js

   {
      creators: [
         {
               "id": 137459,
               "hasTwitch": true,
               "twitchConnections": [
                  {
                     "twitchId": 10488316,
                     "twitchLogo": "https://static-cdn.jtvnw.net/jtv_user_pictures/57856422-762e-4373-b22a-a58735d974c0-profile_image-300x300.png",
                     "twitchDisplayName": "TeamEnvy",
                     "enabled": false,
                     "online": false,
                     "currentViewers": 0
                  }
               ],
               "hasYoutube": true,
               "youtubeConnections": [
                  {
                     "youtubeId": "UCZyoek-4iDviS-yIuJKUh2Q",
                     "youtubeLogo": "https://yt3.ggpht.com/ytc/AAUvwngFUYMT3mmFtOJzEf7WrZLO3cQcZkSKSnjJIGprtA=s88-c-k-c0x00ffffff-no-rj",
                     "youtubeDisplayName": "Envy",
                     "youtubeBroadcastId": "",
                     "enabled": false,
                     "online": false,
                     "currentViewers": 0
                  }
                  ...
               ],
               "hasFacebook": false,
               "facebookConnections": [],
               "hasTwitter": true,
               "twitterConnections": [
                  {
                     "twitterId": "115038550",
                     "twitterName": "Envy",
                     "twitterDisplayName": "Envy",
                     "twitterLogo": "https://pbs.twimg.com/profile_images/1375486379531104259/bBrCuYV3_normal.png",
                     "online": false,
                     "currentViewers": 0
                  }
                  ...
               ],
               "live": false,
               "logo": "https://static-cdn.jtvnw.net/jtv_user_pictures/57856422-762e-4373-b22a-a58735d974c0-profile_image-300x300.png",
         }
      ]
   }
