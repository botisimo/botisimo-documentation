# !bridge (Discord only)
A Discord bridge is a way to send messages between multiple Discord servers running Botisimo.

The `!bridge` command is used to create/join/leave/delete Discord bridges via chat.

  - `delete` - Delete or leave a bridge [view docs](#delete)
  - `join` - Join a bridge [view docs](#join)
  - `new` - Create a new bridge to host [view docs](#new)

If a command argument is required it will be wrapped in `< >` and if the argument is optional it will be wrapped in `[ ]`.

## delete
Delete a bridge

#### Usage
!bridge delete

#### Example
    !bridge delete

Deletes the entire bridge if you are the host. Disconnects from the bridge if you are not the host.

`!bridge delete` -> `Bridge deleted`

## join
Join a bridge using a token

#### Usage
!bridge `<token>`

#### Example
    !bridge ggh4jd7f

Joins the bridge with token `ggh4jd7f`

`!bridge ggh4jd7f` -> `You have been connected to the bridge`

## new
Create a new bridge

#### Usage
!bridge

#### Example
    !bridge

Creates a new bridge and returns a token for other channels to join the bridge

`!bridge` -> `This channel is now hosting a bridge. Add other channels to this bridge by typing '!bridge ggh4jd7f' in those channels.`
