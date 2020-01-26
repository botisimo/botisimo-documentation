# $[cooldown]
Directs the bot to enforce a cooldown in seconds for the command

## Usage
$[cooldown `<seconds>`]

## Example
    $[cooldown 30] This response will be sent only if 30 seconds has passed

Sends the response if it has been 30 seconds since the last time the user sent the command

`!cool` -> `This response will be sent only if 30 seconds has passed`

If it has not been long enough to meet the cooldown they will receive a direct message explaining

`!cool` -> `You must wait 30 seconds between !cool commands`
