import discord #Imports Discord dependencies

client = discord.Client()

# Anything that happens is an event

# Event Listeners
@client.event
async def on_ready():
    print("Bot is now online")

@client.event
async def on_message(message):
    # Checks if message is from user
    if message.author == client.user:
        return
    if message.content == 'hello':
        # Sends message
        await message.channel.send('Hi!')
    if message.content == 'cool':
        # Use Unicode for emojies
        # + -> 000
        # Escape the U
        await message.add_reaction('\U0001F60E')

@client.event
# Displays edit the user has made to the message
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')
# Token on Developer portal
client.run('Paste token here') 
