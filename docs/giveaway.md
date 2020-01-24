# !giveaway
The `!giveaway` command is used to create/view/close/end [giveaways](/account/giveaways) via chat

**NOTE:** You can display the active giveaway in your stream using the [stream overlay](/account/overlays) for giveaways

  - `close` - Close entry for the current giveaway [view docs](#close)
  - `end` - End a giveaway [view docs](#end)
  - `new` - Create a new giveaway [view docs](#new)
  - `open` - Open entry for the current giveaway [view docs](#open)
  - `rules` - View the rules for the current giveaway [view docs](#rules)
  - `view` - View current giveaway [view docs](#view)
  - `winner` - Select a winner [view docs](#winner)

If a command argument is required it will be wrapped in `< >` and if the argument is optional it will be wrapped in `[ ]`.

## close
Closes the giveaway to stop further entry, but keeps the results live

#### Usage
!giveaway close

#### Example
    !giveaway close

## end
Ends the giveaway

#### Usage
!giveaway end

#### Example
    !giveaway end

## new
Create a new giveaway. This will end the current giveaway if it exists.

#### Usage
!giveaway new `<title>` | `[cost=0]` | `[multiple_entries]` | `[max_entries=0]` | `[multiple_wins]`

#### Example
    !giveaway new Xbox Controller Giveaway | 1500 | 1 | 0 | 1

Creates a new giveaway with the title `Xbox Controller Giveaway` that costs `1500` currency to enter. This giveaway allows unlimited entries per user and allows them to win multiple times.

## open
Opens the giveaway to allow entry

#### Usage
!giveaway open

#### Example
    !giveaway open

## rules
Get the rules for the current giveaway

#### Usage
!giveaway rules

#### Example
    !giveaway rules

Outputs the current giveaway rules to the chat. If there is no giveaway or no rules then there is no response

## view
Get the current giveaway info

#### Usage
!giveaway

#### Example
    !giveaway

Outputs the current giveaway to the chat. If there is no giveaway then there is no response

## winner
Select a random winner for the giveaway

#### Usage
!giveaway winner

#### Example
    !giveaway winner

Selects a random winner for the giveaway
