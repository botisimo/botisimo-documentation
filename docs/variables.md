# Response Variables
Response variables are used to make dynamic [custom command](/account/commands) responses. See also [response directives](/docs/directives).

  - `Arguments` - Resolve arguments from command [view docs](#arguments)
  - `bot` - Resolve bot username [view docs](#bot)
  - `botplain` - Resolve bot username without @ symbol [view docs](#botplain)
  - `cache` - Resolve a value from the cache [view docs](#cache)
  - `channel` - Resolve the channel name [view docs](#channel)
  - `count` - Resolve the number of times the command has been used [view docs](#count)
  - `countdown` or `countup` - Resolve time between now and given date [view docs](#countdown)
  - `currency` - Resolve the currency amount for the command issuer [view docs](#currency)
  - `discord` - Show text in Discord chat only [view docs](#discord)
  - `fetch` - Resolve response from the url with GET request [view docs](#fetch)
  - `fetchp` - Resolve response from the url with POST request [view docs](#fetchp)
  - `hours` - Resolve the hours for the command issuer [view docs](#hours)
  - `js` - Resolve javascript expression [view docs](#js)
  - `lastfm` - Resolve the last scrobbled song from lastfm [view docs](#lastfm)
  - `level` - Resolve the level of the command issuer [view docs](#level)
  - `minutes` - Resolve the minutes for the command issuer [view docs](#minutes)
  - `mixer` - Show text in Mixer chat only [view docs](#mixer)
  - `pick` or `random` - Resolve random response from options [view docs](#pick)
  - `query` - Resolve the query string from the command [view docs](#query)
  - `rank` - Resolve the rank of the command issuer [view docs](#rank)
  - `repeat` - Resolves a repeated string [view docs](#repeat)
  - `rng` - Resolve a random number between given numbers [view docs](#rng)
  - `rotate` - Resolve response from options in sequence [view docs](#rotate)
  - `songrequester` - Resolve the requester text of the current song playing on the music player [view docs](#songrequester)
  - `songthumbnail` - Resolve the url to the thumbnail of the current song playing on the music player [view docs](#songthumbnail)
  - `songtitle` - Resolve the title of the current song playing on the music player [view docs](#songtitle)
  - `songurl` - Resolve the url of the current song playing on the music player [view docs](#songurl)
  - `songusername` - Resolve the requester username of the current song playing on the music player [view docs](#songusername)
  - `streamer` - Resolve streamer username [view docs](#streamer)
  - `streamerplain` - Resolve streamer username without @ symbol [view docs](#streamerplain)
  - `stripchar` - Strip a character from text [view docs](#stripchar)
  - `target` - Resolve targeted username from command [view docs](#target)
  - `targetplain` - Resolve targeted username from command without @ symbol [view docs](#targetplain)
  - `total` - Resolve the total number of users [view docs](#total)
  - `twitch` - Show text in Twitch chat only [view docs](#twitch)
  - `urlencode` - Resolve the text as a url encoded string (to be used with `url` variable) [view docs](#urlencode)
  - `userid` - Resolve user id of the command issuer [view docs](#userid)
  - `username` - Resolve username of the command issuer as a mention [view docs](#username)
  - `usernameplain` - Resolve username of the command issuer as plain text [view docs](#usernameplain)
  - `usertype` - Resolve user type of the command issuer (everyone, regular, subscriber, moderator, admin) [view docs](#usertype)
  - `winner` - Resolve the username as a mention of a random user currently online in the channel [view docs](#winner)
  - `xp` - Resolve the xp of the command issuer [view docs](#xp)
  - `youtube` - Show text in Youtube chat only [view docs](#youtube)
  - [Advanced Example](#advanced-example)

If a variable requires a parameter it will be wrapped in `< >` and if the parameter is optional it will be wrapped in `[ ]`.

## Arguments
Resolves the argument from the command input

#### Usage
$(`<argument>` `[fallback]`)

#### Example
    $(2 default text)

Outputs the 2nd argument after the command and optionally uses the `fallback` text if no argument found

`!example this is a test` -> `is`

`!example this` -> `default text`

## bot
Resolve bot username

#### Usage
$(bot)

#### Example
    $(bot) is here!

`!checkin` -> `@botisimo is here!`

## botplain
Resolve bot username without @ symbol

#### Usage
$(botplain)

#### Example
    $(botplain) is here!

`!checkin` -> `botisimo is here!`

## cache
Resolve a value from the cache

Values can be save to the cache using the [cache directive](/docs/directives#cache).

#### Usage
$(cache `<key>`)

#### Example
    You have a cached value of "$(cache $(username))"

Outputs the value in the cache for the username, if any

`!cache` -> `You have a cached value of "some value to save for later"`

## channel
Resolves the current channel name

#### Usage
$(channel)

#### Example
    Welcome to $(channel)!

`!channel` -> `Welcome to #bob!`

## count
Resolve the number of times the command has been used

#### Usage
$(count)

#### Example
    This command has been used $(count) times

`!count` -> `This command has been used 25 times`

## countdown
Resolves the time between now and the given date

#### Usage
$(countdown `<date>`)

#### Example
    The new year begins in $(countdown 1/1/2018 00:00:00)

`!countdown` -> `The new year begins in 30 days 12 hours 37 minutes`

## currency
Resolves the command issuers currency amount

#### Usage
$(currency)

#### Example
    Currency: $(currency)

Outputs `375` if the user's has `375` currency

`!currency` -> `Currency: 375`

## discord
Resolves the text only when responding via Discord chat. Works the same as [$(twitch)](#twitch).

## fetch
Resolves the response from the url using a GET request

#### Usage
$(fetch `<url>`)

#### Example
    $(fetch https://foaas.com/you/Peter/Bob)

`!foaas` -> `Fuck you, Peter. -Bob`

## fetchp
Same as [$(fetch)](#fetch) but with POST request

## hours
Resolves the number of hours the command issuers has watched the live stream

#### Usage
$(hours)

#### Example
    Hours: $(hours)

Outputs `9.28` if the user has watched for `557` minutes

`!hours` -> `Hours: 9.28`

## js
Resolves the value of a javascript expression

#### Usage
$(js `<javascript>`)

#### Example
    $(js ['need', 'a', 'better', 'example'].join(' '))

`!js` -> `need a better example`

## lastfm
Resolves the last scrobbled song from lastfm for the given username (must be lastfm username)

#### Usage
$(lastfm `<username>`)

#### Example
    $(lastfm botisimo)

`!lastfm` -> `Egzod - Universe`

## level
Resolves the command issuers level

#### Usage
$(level)

#### Example
    Get on my level: $(level)

Outputs `5` if the user's level is `5`

`!level` -> `Get on my level: 5`

## minutes
Resolves the number of minutes the command issuers has watched the live stream

#### Usage
$(minutes)

#### Example
    Minutes: $(minutes)

Outputs `600` if the user has watched for `600` minutes

`!minutes` -> `Minutes: 600`

## mixer
Resolves the text only when responding via Mixer chat. Works the same as [$(twitch)](#twitch).

## pick
Resolves a random response from the given options

#### Usage
$(pick `<option>` | `[option]` | `[option]` | ...)

#### Example
    I'm thinking...$(pick yes | no | maybe so | I don't know)

`!pick` -> `I'm thinking...maybe so`

`!pick` -> `I'm thinking...yes`

## query
Resolves the query string from the command

#### Usage
$(query `[offset]`)

#### Example
    $(query 2) $(query)

Outputs the query string starting with the 2nd word then the full query string

`!query this is the query` -> `is the query this is the query`

## rank
Resolves the command issuers rank

#### Usage
$(rank)

#### Example
    You are rank: $(rank)

Outputs `5` if the user's rank is `5`

`!rank` -> `You are rank: 5`

## repeat
Resolves a repeated string

#### Usage
$(repeat `<count>` `<string>`)

#### Example
    $(repeat 5 PogChamp Kappa)

`!repeat` -> `PogChamp Kappa PogChamp Kappa PogChamp Kappa PogChamp Kappa PogChamp Kappa`

## rng
Resolve a random number between given numbers

#### Usage
$(rng `<min>` `<max>`)

#### Example
    You rolled a $(rng 1 100)

Outputs a randomly selected number between 1 and 100 (including 1 and 100)

`!roll` -> `You rolled a 76`

`!roll` -> `You rolled a 33`

## rotate
Resolves a response from the given options in sequence

#### Usage
$(rotate `<option>` | `[option]` | `[option]` | ...)

#### Example
    $(rotate First response | Second response | Third response)

`!rotate` -> `First response`

`!rotate` -> `Second response`

`!rotate` -> `Third response`

`!rotate` -> `First response`

## songrequester
Resolve the requester text of the current song playing on the [music player](/account/music)

#### Usage
$(songrequester)

#### Example
    Now Playing: $(songtitle)$(songrequester)

Outputs ` (requested by @username)` if the song was requested by a user or outputs nothing if the song was added via web UI

`!song` -> `Now Playing: Culture Code - Make Me Move (feat. Karra) [NCS Release] (requested by @username)`

## songthumbnail
Resolve the url to the thumbnail of the current song playing on the [music player](/account/music)

#### Usage
$(songthumbnail)

#### Example
    $(songthumbnail)

`!songthumbnail` -> `https://i1.ytimg.com/vi/vBGiFtb8Rpw/mqdefault.jpg`

## songtitle
Resolves the title of the song currently set to play on the [music player](/account/music)

#### Usage
$(songtitle)

#### Example
    Now Playing: $(songtitle)

`!song` -> `Now Playing: Culture Code - Make Me Move (feat. Karra) [NCS Release]`

## songurl
Resolves the url of the song currently set to play on the [music player](/account/music)

#### Usage
$(songurl)

#### Example
    Now Playing: $(songurl)

`!song` -> `Now Playing: https://youtube.com/watch?v=vBGiFtb8Rpw`

## songusername
Resolve the requester text of the current song playing on the [music player](/account/music)

#### Usage
$(songusername)

#### Example
    Now Playing: $(songtitle) ($(songusername))

`!song` -> `Now Playing: Culture Code - Make Me Move (feat. Karra) [NCS Release] (@username)`

## streamer
Resolve streamer username

#### Usage
$(streamer)

#### Example
    $(streamer) is live Mon-Fri 12-3pm!

`!schedule` -> `@streamername is live Mon-Fri 12-3pm!`

## streamerplain
Resolve streamer username without @ symbol

#### Usage
$(streamerplain)

#### Example
    $(streamerplain) is here!

`!schedule` -> `streamername is live Mon-Fri 12-3pm!`

## stripchar
Strip a character from text

#### Usage
$(stripchar `<character>` `<text>`)

#### Example
    $(1) is one cool streamer, check them out at https://mixer.com/$(stripchar @ $(1))

`!shoutout @username` -> `@username is one cool streamer, check them out at https://mixer.com/username`

## target
Resolve targeted username from command

#### Usage
$(target)

#### Example
    Shout out to $(target)!

`!shoutout @bob` -> `Shout out to @bob!`

## targetplain
Resolve targeted username from command without @ symbol

#### Usage
$(targetplain)

#### Example
    Go to mixer.com/$(targetplain) and drop a follow!

`!follow @bob` -> `Go to mixer.com/bob and drop a follow!`

## total
Resolves the total numbers of ranked users

#### Usage
$(rank)

#### Example
    Total users: $(total)

Outputs `300` if the there are `300` ranked users

`!total` -> `Total users: 300`

## twitch
Resolves the text only when responding via Twitch chat

#### Usage
$(twitch `<message>`)

#### Example
    You are a $(twitch super awesome and) cool dude$(twitch !)

Outputs "You are a super awesome and cool dude!" when responding via Twitch chat

`!example` -> twitch -> `You are a super awesome and cool dude!`

`!example` -> mixer/youtube/discord -> `You are a cool dude`

## urlencode
Resolves a url encoded string

#### Usage
$(urlencode `<string>`)

#### Example
    $(urlencode please encode me)

`!encode` -> `please%20encode%20me`

## userid
Resolves the command issuer's user id for the platform the command was issued

#### Usage
$(userid)

#### Example
    Your user id is $(userid)

`!id` -> `Your user id is 837455`

## username
Resolves the command issuer's username as a mention

#### Usage
$(username)

#### Example
    Hi, $(username)!

`!hi` -> twitch/mixer/youtube -> `Hi, @bob!`

`!hi` -> discord -> `Hi, <@112338494039>!`

## usernameplain
Resolves the command issuer's username as plain text

#### Usage
$(usernameplain)

#### Example
    Hi, $(usernameplain)!

`!hi` -> twitch/mixer/youtube -> `Hi, bob!`

`!hi` -> discord -> `Hi, bob!`

## usertype
Resolves the command issuer's user type (everyone, regular, subscriber, moderator, admin)

#### Usage
$(usertype)

#### Example
    Your user type is $(usertype)

`!type` -> `Your user type is moderator`

## winner
Resolve the username as a mention of a random user currently online in the channel

#### Usage
$(winner `[minutes=10]` `[keyword=]`)

#### Example
    The winners is $(winner 5 enter)!

Outputs a randomly selected user who is online and sent the message "enter" in the last 5 minutes. The keyword is case sensitive.

`!winner` -> `The winner is @gary!`

## xp
Resolves the command issuers xp

#### Usage
$(xp)

#### Example
    You have $(xp) XP

Outputs `5,000` if the user has `5,000` xp

`!xp` -> `You have 5,000 XP`

## youtube
Resolves the text only when responding via Youtube chat. Works the same as [$(twitch)](#twitch).

## Advanced Example
This example shows you how to combine the `$(fetch)`, `$(urlencode)`, and `$(query)` response variables to make a !ascii command that translates the user's input into formatted ASCII text for Discord

#### Example
    ```$(fetch http://artii.herokuapp.com/make?text=$(urlencode $(query))&font=colossal)```

`!ascii Hello World` ->

```text
888    888          888 888              888       888                  888      888
888    888          888 888              888   o   888                  888      888
888    888          888 888              888  d8b  888                  888      888
8888888888  .d88b.  888 888  .d88b.      888 d888b 888  .d88b.  888d888 888  .d88888
888    888 d8P  Y8b 888 888 d88""88b     888d88888b888 d88""88b 888P"   888 d88" 888
888    888 88888888 888 888 888  888     88888P Y88888 888  888 888     888 888  888
888    888 Y8b.     888 888 Y88..88P     8888P   Y8888 Y88..88P 888     888 Y88b 888
888    888  "Y8888  888 888  "Y88P"      888P     Y888  "Y88P"  888     888  "Y88888
```
