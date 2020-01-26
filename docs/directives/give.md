# $[give]
Directs the bot to give currency to the user who uses the command or optionally the targeted user

## Usage
$[give `<amount>` `[target]`]

## Example
    $[give 50] You just received 50 Goldfrags for using this command, woo!

Gives 50 currency to the user when they use the command and outputs the response

`!give` -> `You just received 50 Goldfrags for using this command, woo!`

## Example
    $[give 50 $(1)] $(1) just received 50 Goldfrags, woo!

Gives 50 currency to the targeted user when the command is used and outputs the response

`!give @username` -> `@username just received 50 Goldfrags, woo!`
