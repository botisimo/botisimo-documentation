# !command
The `!command` command is used to create/edit/delete/enable/disable [custom commands](https://botisimo.com/account/commands) via chat

  - `delete` - Delete command [view docs](#delete)
  - `disable` - Disable command [view docs](#disable)
  - `edit` - Edit command response [view docs](#edit)
  - `enable` - Enable command [view docs](#enable)
  - `info` - View command info [view docs](#info)
  - `list` - List commands [view docs](#list)
  - `new` - Create a new command [view docs](#new)
  - `permission` - Edit command minimum permission [view docs](#permission)

If a command argument is required it will be wrapped in `< >` and if the argument is optional it will be wrapped in `[ ]`.

**NOTE:** Commands are enabled and disabled based on the platform (Twitch, Mixer, Youtube, etc.) the command was issued from. Commands will respond to the channel they are called from.

## delete
Delete command

#### Usage
!command delete `<name>`

#### Example
    !command delete !social

Deletes the command named `!social`

## disable
Disable command

#### Usage
!command disable `<name>`

#### Example
    !command disable !social

Disables the command named `social` but does not delete it

## edit
Edit command response

#### Usage
!command edit `<name>` `<response>`

#### Example
    !command edit !social You can follow me on twitter and instagram @botisimo

Edits the command named `!social` to respond with `You can follow me on twitter and instagram @botisimo`

## enable
Enable command

#### Usage
!command enable `<name>`

#### Example
    !command enable !social

Enables the command named `social`

## info
Get info for a command

#### Usage
!command info `<name>`

#### Example
    !command info !social

Outputs the details for the `!social` command

## list
List commands

#### Usage
!command list

#### Example
    !command list

Lists commands available in Botisimo

## new
Create a new command

#### Usage
!command new `<name>` `<response>`

#### Example
    !command new !social You can follow me on twitter @botisimo

Creates a new command named `!social` that responds with `You can follow me on twitter @botisimo`

## permission
Edit command minimum permission

#### Usage
!command permission `<name>` `<permission=everyone|regs|subs|mods|admin>`

#### Example
    !command permission !social everyone

Edits the minimum permission for the command named `!social` to allow `everyone` to use it
