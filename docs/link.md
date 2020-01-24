# !link

The `!link` command is used to link users from different platforms together to share currency and XP. Each group of linked users can have 1 user from each platform linked (twitch, mixer, youtube, and discord). You must have login access to the user account on each platform to be able to link them.

  - [Link Users](#link-users)
  - [Check Linked Users](#check-linked-users)
  - [Unlink Users](#unlink-users)

## Link Users

Log in to a chat platform (in this example we'll use Twitch) and join the channel with Botisimo and initiate the linking process by targeting another platform and username:

```
(twitch) Player1: !link mixer Player1
```

If the targeted user is not in the system, you may need to log in and send a message in chat to allow Botisimo to register that user to the system. If the user is in the system, Botisimo will respond with instructions to complete the link:

```
(twitch) Botisimo: Link initiated. Please log in to mixer as Player1 and type "!link twitch Player1" to finish linking with Player1 [twitch]
```

Log in to the your user on the other platform (in this example we are using Mixer) and complete the link

```
(mixer) Player1: !link twitch Player1
```

If everything is correct, Botisimo will let you know your users have been linked:

```
(mixer) Botisimo: Player1 [mixer] has been linked with Player1 [twitch]
```

That's it! To link another user you would just repeat the steps:

```
(twitch) Player1: !link discord Player1
(twitch) Botisimo: Link initiated. Please log in to discord as Player1 and type "!link twitch Player1" to finish linking with Player1 [twitch], Player1 [mixer]
```
```
(discord) Player1: !link twitch Player1
(discord) Botisimo: Player1 [discord] has been linked with Player1 [twitch], Player1 [mixer]
```

## Check Linked Users

You can use `!link` to see what users are linked together:

```
(twitch) Player1: !link
(twitch) Botisimo: Player1 [twitch], Player1 [mixer], Player1 [discord]
```

## Unlink Users

To unlink a user you can target a platform with the `!unlink` command

```
(twitch) Player1: !unlink discord
(twitch) Botisimo: Player1 [discord] has been unlinked
(twitch) Player1: !link
(twitch) Botisimo: Player1 [twitch], Player1 [mixer]
```
