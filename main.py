# This is going to be the main Python file for the Hackathon Chatbot

import discord

#import os

# Define bot's intents/permissions
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.reactions = True
intents.members = True

# Initialize the bot client with intents
client = discord.Client(intents=intents)

# Triggered when bot is ready
@client.event
async def on_ready():
    print(f'Bot logged in as: {client.user}')

# Triggered when anyone sends a message
@client.event
async def on_message(message):
    # If sender is bot, ignore it
    if message.author == client.user:
        return
    
    # If message starts with 'hello', bot will respond
    if message.content.startswith('hello'):
        await message.channel.send(f'Hello {message.author.mention}! I am a basic Discord bot.')

# Run the bot with your Discord bot token THIS IS WHERE TO PUT THE KEY THEY GIVE US
client.run('BOT_TOKEN_HERE')

# client.run(os.getenv('TOKEN'))
# This code will access the token from the env page
# This is only used if the token is made public to other users online