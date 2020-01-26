# $(cache)
Resolve a value from the cache

Values can be save to the cache using the [cache directive](</directives/cache>).

## Usage
$(cache `<key>`)

## Example
    You have a cached value of "$(cache $(username))"

Outputs the value in the cache for the username, if any

`!cache` -> `You have a cached value of "some value to save for later"`
