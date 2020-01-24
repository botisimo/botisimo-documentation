# Available Commands
Commands are used to allow you and your moderators/users to interact with the bot via chat

Below is a list of the default commands available with Botisimo. They are grouped according to the default permission settings but the settings may differ per account. If a command argument is required it will be wrapped in `< >` and if the argument is optional it will be wrapped in `[ ]`.

**NOTE:** If users are **NOT** receiving whispers from Botisimo in Twitch, they may need to send it a whisper first to get it working for their account.

## Public Commands

#### All platforms

  - `!amazon <query>` - Search Amazon products*. Returns top 10 results in Discord and top result in Twitch, Mixer, & Youtube
  - `!buy <key>` - Purchase an item from the shop using currency
  - `!clip [username]` - Responds with the top Twitch clip for the current user or the `username` (must be a twitch username)
  - `!commands` - Receive list of custom commands available to you via whisper
  - `!enter` - Enter the giveaway [view docs](/docs/enter)
  - `!help` - Link to Botisimo docs
  - `!leaderboard` - Display link to the leaderboard
  - `!optin` - Opt in to Level Up and DyneOps announcements for your user
  - `!optout` - Opt out of Level Up and DyneOps announcements for your user
  - `!queue` - Join or leave player queue [view docs](/docs/queue)
  - `!rank [username]` - Display rank information for the current user or the `username`
  - `!reddit <subreddit>` - Get the latest post(s) for a subreddit. Returns top 10 results in Discord and top result in Twitch & Mixer
  - `!shop` - Display available shop items for channel in chat
  - `!songrequest <youtube_video_url>` or `!sr <youtube_video_url>` - Request a song (works with the [music player](/account/music))
  - `!stackoverflow <query>` - Search Stackoverflow questions. Returns top 10 results in Discord and top result in Twitch & Mixer
  - `!twit <username>` or `!twitter <username>` - Responds with the latest tweet from the given `username` (must be a twitter username)
  - `!vote` - Vote in poll [view docs](/docs/vote)
  - `!wikipedia <topic>` or `!wiki <topic>` - Search Wikipedia topics. Returns top 10 results in Discord and top result in Twitch & Mixer

#### Twitch, Mixer, & Youtube only

  - `!live` - Force a stream up announcement in Discord (useful in case the automatic announcement fails)
  - `!uptime` - Display time the stream started in chat

#### Discord only

  - `!login [platform=twitch]` - Receive a link to authorize chat mirroring for your Discord user (platform can be `twitch` or `mixer`)
  - `!logout [platform=twitch]` - Disable chat mirroring for your Discord user (platform can be `twitch` or `mixer`)
  - `!playlists` - List Youtube playlists from connected account (must have [linked youtube account](/account/connections))

## Mod Commands

#### All platforms

  - `!command` - Manage custom commands [view docs](/docs/command)
  - `!gameall <game>` - Set the game on all connections on the account
  - `!give <amount> <username> [username] [username] ...` - Give currency to 1 or more users
  - `!give <amount> all` - Give currency to everyone
  - `!give <amount> chat` - Give currency to everyone currently in chat
  - `!giveaway` - Manage giveaways [view docs](/docs/giveaway)
  - `!irregular <username>` - Remove this user from regulars
  - `!nextsong` or `!ns` - Skip the current song (works with the [music player](/account/music))
  - `!ping` - Responds with `pong` in chat (quick way to check if Botisimo is responding in your channel)
  - `!poll` - Manage polls [view docs](/docs/poll)
  - `!regular <username>` - Add this user to regulars
  - `!timer` - Manage custom timers [view docs](/docs/timer)
  - `!titleall <title>` - Set the title on all connections on the account
  - `!winner [message] [|minutes]` - Pick a random winner from chat who sent a message in last 10 minutes. Optionally, use the `message` to filter users who typed a specific message (default: any message). You can also alter the minutes by using the `|` character followed by a number (example: `!winner enter|30`)

#### Twitch, Mixer, & YouTube only

  - `!game [game=]` - Get or set the game for the stream
  - `!title [title=]` - Get or set the title for the stream

#### Discord only

  - `!bridge` - Manage Discord bridges [view docs](/docs/bridge)
  - `!clear <number>` - Clear a number of messages from the chat (max: 99)
  - `!subscribe <platform> <username>` - Subscribe to other Botisimo users' stream up announcements (platform should be `twitch` or `mixer`)
  - `!unsubscribe <platform> <username>` - Unsubscribe from other Botisimo users' stream up announcements (platform should be `twitch` or `mixer`)

## Admin Commands

#### All platforms

  - `!leave` - Disable Botisimo for your channel (can be reenabled on the [connections page](/account/connections) of your account)
  - `!prefix [prefix=]` - Get or set the Botisimo command prefix (only affects Botisimo's built-in commands)

###### * We are a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for us to earn fees by linking to Amazon.com and affiliated sites.
