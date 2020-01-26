# Arguments
Resolves the argument from the command input

## Usage
$(`<argument>` `[fallback]`)

## Example
    $(2 default text)

Outputs the 2nd argument after the command and optionally uses the `fallback` text if no argument found

`!example this is a test` -> `is`

`!example this` -> `default text`
