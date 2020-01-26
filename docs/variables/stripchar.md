# $(stripchar)
Strip a character from text

## Usage
$(stripchar `<character>` `<text>`)

## Example
    $(1) is one cool streamer, check them out at https://mixer.com/$(stripchar @ $(1))

`!shoutout @username` -> `@username is one cool streamer, check them out at https://mixer.com/username`
