# !poll
The `!poll` command is used to create/view/close/end [polls](https://botisimo.com/account/polls) via chat

**NOTE:** You can display the active poll in your stream using the [stream overlay](https://botisimo.com/account/overlays) for polls

  - `close` - Close voting for a poll [view docs](#close)
  - `end` - End a poll [view docs](#end)
  - `new` - Create a new poll [view docs](#new)
  - `open` - Open voting for a poll [view docs](#open)
  - `view` - View current poll [view docs](#view)
  - `winner` - Select a winner [view docs](#winner)

If a command argument is required it will be wrapped in `< >` and if the argument is optional it will be wrapped in `[ ]`.

## close
Closes the poll to stop further voting, but keeps the results live

#### Usage
!poll close

#### Example
    !poll close

## end
Ends the poll

#### Usage
!poll end

#### Example
    !poll end

## new
Create a new poll. This will end the current poll if it exists.

#### Usage
!poll new `<option>` | `[option]` | `[option]` | ...

#### Example
    !poll new Is this a fun poll? | yes | no | hell no | what a stupid poll

Creates a new poll with the options `yes`, `no`, `hell no`, and `what a stupid poll`

## open
Opens the poll to allow voting

#### Usage
!poll open

#### Example
    !poll open

## view
Get the current poll info

#### Usage
!poll

#### Example
    !poll

Outputs the current poll and standings to the chat. If there is no poll there is no response

## winner
Select a random winner from the given option

#### Usage
!poll winner `<option>`

#### Example
    !poll winner 1

Sets the winning option to option `1` and rewards and users who voted on that option with currency based on their bet
