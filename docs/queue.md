# !queue
The `!queue` command is used to join/leave/list users in the queue via chat

  - `clear` - Clear the queue [view docs](#clear)
  - `close` - Close the queue [view docs](#close)
  - `join` - Join the queue [view docs](#join)
  - `leave` - Leave the queue [view docs](#leave)
  - `list` - List users in queue [view docs](#list)
  - `next` - Get the next user in the queue [view docs](#next)
  - `open` - Open the queue [view docs](#open)
  - `permission` - Edit queue minimum permission [view docs](#permission)
  - `random` - Gets a random user in the queue as the next user [view docs](#random)

## clear
Clear the queue

#### Usage
!queue clear

#### Example
    !queue clear

Clears everyone from the queue

## close
Close the queue

#### Usage
!queue close

#### Example
    !queue close

Closes the queue

## join
Join the queue

#### Usage
!queue join

#### Example
    !queue join

Joins the command issuer to the queue

## leave
Leave the queue

#### Usage
!queue leave

#### Example
    !queue leave

Removes the command issuer from the queue

## list
List queue

#### Usage
!queue list

#### Example
    !queue list

Lists users in the queue

## next
Retrieve the next user(s) from the queue

#### Usage
!queue next `[users=1]`

#### Example
    !queue next 5

Outputs the name(s) of the next user(s) in the queue and removes them from the queue. Default is 1 user

## open
Open the queue

#### Usage
!queue open

#### Example
    !queue open

Opens the queue

## permission
Edit queue minimum permission

#### Usage
!queue permission `<permission=everyone|regs|subs|mods|admin>`

#### Example
    !queue permission regular

Edits the minimum permission for the queue to allow only `regular` users and above to use it

## random
Retrieve a random user from the queue as the next user

#### Usage
!queue random

#### Example
    !queue random

Outputs the name of the randomly selected user in the queue and removes them from the queue
