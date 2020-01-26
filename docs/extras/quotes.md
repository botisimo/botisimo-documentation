# Twitch.Center Quote System
Botisimo does not have a quote system, however you can use the `$(fetch)`, `$(query)`, and `$(urlencode)` [response variables](</variables>) combined with a third-party api to make your own.

## What can it do?

- Allow users to add quotes
- Allow users to delete quotes
- Respond with random quote
- Respond with specific quote

## How do I make it?

#### Step 1.
Generate three command responses to use in the commands by visiting this URL: https://twitch.center/customapi/quote/generate

```text
$(urlfetch http://twitch.center/customapi/quote?token=********&data=$(querystring))
$(urlfetch http://twitch.center/customapi/addquote?token=********&data=$(querystring))
$(urlfetch http://twitch.center/customapi/delquote?token=********&data=$(querystring))
```

In the generated command responses, there is a token (represented by asterisks `*` in the example above). **Keep this token a secret!**

#### Step 2.
In the command responses that are generated.

Find `urlfetch` and replace it with `fetch`

Find `$(querystring)`
- **Only** in the `/addquote?` command response, replace it with: `$(urlencode $(query))`
- In the other two, replace it with: `$(query)`

It should look like this now
```text
$(fetch http://twitch.center/customapi/quote?token=********&data=$(query))
$(fetch http://twitch.center/customapi/addquote?token=********&data=$(urlencode $(query)))
$(fetch http://twitch.center/customapi/delquote?token=********&data=$(query))
```

#### Step 3.
Create a [custom command](https://botisimo.com/account/commands) for each one.

```
name: !quote
response: $(fetch http://twitch.center/customapi/quote?token=********&data=$(query))
```

```
name: !addquote
response: $(fetch http://twitch.center/customapi/addquote?token=********&data=$(urlencode $(query)))
```

```
name: !delquote
response: $(fetch http://twitch.center/customapi/delquote?token=********&data=$(query))
```

Remember to set the appropriate permissions! For example, you might not want everyone to be able to delete quotes.

##### Special thanks to @Tylegn & @Superlisaa
