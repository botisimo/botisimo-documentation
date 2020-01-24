# Response Directives
Response directives are used to make dynamic actions for your [custom commands](https://botisimo.com/account/commands). Directives will be processed after [response variables](</variables>) and in the order they appear in the response text.

  - `cache` - Cache a value [view docs](#cache)
  - `chain` - Chain multiple responses together [view docs](#chain)
  - `cooldown` - Add a cooldown (in seconds) to the command [view docs](#cooldown)
  - `cost` - Add a currency cost to the command [view docs](#cost)
  - `delay` - Add a delay (in seconds) to the command response [view docs](#delay)
  - `delete` - Delete the command message [view docs](#delete)
  - `discord role add` - Add discord role to user [view docs](#discord-role-add)
  - `discord role check` - Require a user to have a discord role [view docs](#discord-role-check)
  - `discord role remove` - Remove discord role from user [view docs](#discord-role-remove)
  - `event` - Send a custom event to the event overlay [view docs](#event)
  - `give` - Give the user currency [view docs](#give)
  - `hours` - Add an hours requirement to the command [view docs](#hours)
  - `norelay` - Do not relay the response to other platforms [view docs](#norelay)
  - `precooldown` - Add a cooldown (in seconds) to the command before parsing variables [view docs](#precooldown)
  - `precost` - Add a currency cost to the command before parsing variables [view docs](#precost)
  - `predelay` - Add a delay (in seconds) to the command response before parsing command variables [view docs](#predelay)
  - `prehours` - Add an hours requirement to the command before parsing variables [view docs](#prehours)
  - `transfer` - Transfer currency to another user [view docs](#transfer)
  - `whisper` or `dm` - Respond to the user with a direct message [view docs](#whisper)
  - [Advanced Example](#advanced-example)

If a directive requires a parameter it will be wrapped in `< >` and if the parameter is optional it will be wrapped in `[ ]`.

## cache
Saves a value temporarily to be used in other commands

Fetch values from the cache using the [cache variable](</variables:cache>). The cache is not meant to be used as a long term or permanent place to store any sensitive or important information. This cache could be reset at any time without warning.

#### Usage
$[cache `<key>` `<seconds>` `<value>`]

#### Example
    $[cache $(username) 60 some value to save for later] value saved

Saves "some value to save for later" to the cache for 60 seconds

`!cache` -> `value saved`

## chain
Break response into multiple, chained responses

#### Usage
$[chain]

#### Example
    This is the first response $[chain] This is the second response $[chain] This is a third response

Breaks the response into multiple responses

- [Pro members](https://botisimo.com/membership.html) are limited to chaining 3 responses
- [Master members](https://botisimo.com/membership.html) are limited to chaining 5 responses
- [Guild members](https://botisimo.com/membership.html) are limited to chaining 10 responses

`!chain`
 -> `This is the first response`
 -> `This is the second response`
 -> `This is a third response`

## cooldown
Directs the bot to enforce a cooldown in seconds for the command

#### Usage
$[cooldown `<seconds>`]

#### Example
    $[cooldown 30] This response will be sent only if 30 seconds has passed

Sends the response if it has been 30 seconds since the last time the user sent the command

`!cool` -> `This response will be sent only if 30 seconds has passed`

If it has not been long enough to meet the cooldown they will receive a direct message explaining

`!cool` -> `You must wait 30 seconds between !cool commands`

## cost
Directs the bot to add a currency cost to the command

#### Usage
$[cost `<amount>`]

#### Example
    $[cost 50] You just paid 50 Goldfrags to use this command, ha!

Adds a cost of 50 currency to use the command and outputs the response

`!cost` -> `You just paid 50 Goldfrags to use this command, ha!`

If the user does not have enough currency they will receive a direct message explaining

`!cost` -> `Not enough Goldfrags to use that command 37/50`

## delay
Directs the bot to wait some seconds before responding

#### Usage
$[delay `<seconds>`]

#### Example
    $[delay 5] This response will be sent after 5 seconds

Sends the response after waiting 5 seconds

`!delay` -> wait 5 seconds -> `This response will be sent after 5 seconds`


## delete
Directs the bot to delete the command message before responding

#### Usage
$[delete]

#### Example
    $[delete] Your command message was deleted

Deletes the command message before responding

~~`!delete`~~ -> `Your command message was deleted`

## discord role add
Adds a role to the user issuing the command

#### Usage
$[discord role add `<role>`]

#### Example
    $[discord role add wizard] You have been added to the wizard role

Adds the user to the wizard role and responds

`!wizard` -> `You have been added to the wizard role`

## discord role check
Requires a user to have a discord role

#### Usage
$[discord role check `<role>`]

#### Example
    $[discord role check wizard] (∩｀-´)⊃━☆ﾟ.*･｡ﾟ

Checks that the user has the wizard role and responds if they do

`!expelliarmus` -> `(∩｀-´)⊃━☆ﾟ.*･｡ﾟ`

## discord role remove
Removes a role from the user issuing the command

#### Usage
$[discord role remove `<role>`]

#### Example
    $[discord role remove wizard] You have been removed from the wizard role

Removes the user from the wizard role and responds

`!muggle` -> `You have been removed from the wizard role`

## event
Sends a custom event to the [events overlay](https://botisimo.com/account/overlays)

#### Usage
$[event `[text]` | `[subtext]` | `[milliseconds=3000]` | `[thumbnail]` | `[sound]`]

#### Example
    $[event This is the text | This is the subtext | 5000 | https://media2.giphy.com/media/KXtq8oYQrYMIF9Esi7/giphy.gif | http://soundbible.com/grab.php?id=1817&type=mp3] event sent

`!event` -> `event sent`

## give
Directs the bot to give currency to the user who uses the command or optionally the targeted user

#### Usage
$[give `<amount>` `[target]`]

#### Example
    $[give 50] You just received 50 Goldfrags for using this command, woo!

Gives 50 currency to the user when they use the command and outputs the response

`!give` -> `You just received 50 Goldfrags for using this command, woo!`

#### Example
    $[give 50 $(1)] $(1) just received 50 Goldfrags, woo!

Gives 50 currency to the targeted user when the command is used and outputs the response

`!give @username` -> `@username just received 50 Goldfrags, woo!`

## hours
Directs the bot to require minimum hours for the command

#### Usage
$[hours `<hours>`]

#### Example
    $[hours 10] This response will be sent only if the user has watched the stream for 10 hours

Sends the response if the user has watched the stream for 10 hours

`!special` -> `This response will be sent only if the user has watched the stream for 10 hours`

If the user has not watched the stream for long enough they will receive a direct message explaining

`!special` -> `You must watch the stream for 10 hours to unlock the !special command`

## norelay
Directs the bot to not relay the response to this command

#### Usage
$[norelay]

#### Example
    $[norelay] This response will not be sent to other platforms via relay

Sends the response but does not relay it to the other platforms

`!norelay` -> `This response will not be sent to other platforms via relay`

## precooldown
Same as [$[cooldown]](#cooldown) but applied before parsing command variables

## precost
Same as [$[cost]](#cost) but applied before parsing [command variables](</variables>)

## predelay
Same as [$[delay]](#delay) but applied before parsing command variables

## prehours
Same as [$[hours]](#hours) but applied before parsing command variables

## transfer
Directs the bot to transfer currency from the user who uses the command to the targeted user

#### Usage
$[transfer `<amount>` `<target>`]

#### Example
    $[transfer 100 $(1)] You just transferred 100 Goldfrags to $(1) for using this command, woo!

Transfers 100 currency from the user when they use the command and outputs the response

`!transfer @username` -> `You just transferred 100 Goldfrags to @username for using this command, woo!`

If the user does not have enough currency they will receive a direct message explaining

`!transfer @username` -> `Not enough Goldfrags to use that command 37/100`

## whisper
Directs the bot to respond to the command via a direct message

#### Usage
$[whisper]

#### Example
    $[whisper] This response will be sent in a direct message

Sends the response in a direct message

`!whisper` -> `This response will be sent in a direct message`

## Advanced Example
This example shows you how to combine the `$(pick)` and `$(repeat)` [response variables](</variables>) with the `$[cost]` and `$[give]` response directives to make a !gamble command

#### Example
    $[cost 100] $(pick $(repeat 5 $[give 100] You broke even +0 | )$(repeat 5 You lost it all -100 | )$(repeat 5 $[give 150] You got a return on your investment +50 | )$[give 300] You hit the jackpot! +200)

This command will cost the user 100 currency to run and will give them a 5:16 chance to break even, a 5:16 chance to lose it, a 5:16 chance to get a return, and a 1:16 chance to hit the jackpot

`!gamble` -> `You got a return on your investment +50`
