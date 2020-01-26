# !timer
The `!timer` command is used to create/edit/delete/start/stop [custom timers](https://botisimo.com/account/timers) via chat

**NOTE:** Timers are only activated if 10 or more messages have been sent since the last time it was activated

  - `delete` - Delete a timer [view docs](#delete)
  - `edit` - Edit a timer [view docs](#edit)
  - `info` - View timer info [view docs](#info)
  - `list` - List timers [view docs](#list)
  - `new` - Create a new timer [view docs](#new)
  - `start` - Start a timer [view docs](#start)
  - `stop` - Stop a timer [view docs](#stop)

If a command argument is required it will be wrapped in `< >` and if the argument is optional it will be wrapped in `[ ]`.

**NOTE:** Timers are started and stopped based on the platform (Twitch, Mixer, Youtube, or Discord) and channel the command was issued from. Timers will only post to a single channel per platform.

## delete
Delete a timer

#### Usage
!timer delete `<name>`

#### Example
    !timer delete social

Deletes the timer named `social`

## edit
Edit a timer

#### Usage
!timer edit `<name>` `<interval>` `<message>`

#### Example
    !timer edit social 10 Follow me on twitter and instagram @botisimo

Edits the timer named `social` to post the message every 10 minutes in the current channel

## info
Get info for a timer

#### Usage
!timer info `<name>`

#### Example
    !timer info social

Outputs the details for the `social` timer

## list
List timers

#### Usage
!timer list

#### Example
    !timer list

Lists timers available in Botisimo

## new
Create a new timer

#### Usage
!timer new `<name>` `<interval>` `<message>`

#### Example
    !timer new social 5 Follow me on twitter @botisimo

Creates a new timer named `social` that posts the message every 5 minutes in the current channel

## start
Starts a timer in the current channel

#### Usage
!timer start `<name>`

#### Example
    !timer start social

Starts the timer named `social` in the current channel

## stop
Stops a timer

#### Usage
!timer stop `<name>`

#### Example
    !timer stop social

Stops the timer named `social` but does not delete it
