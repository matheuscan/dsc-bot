# This example requires the 'message_content' intent.

import discord
import json
import re
from discord.ext import commands
import re._constants
badwords = ['mierda', 'coño', 'mardicion','maldicion', 'verga', 'vergacion','puta']


intents = discord.Intents.default()
intents.message_content = True
with open('config.json','r') as file:
    data = json.load(file)
bot  = commands.Bot(command_prefix='$')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        author = message.author
        content = message.content.split(" ")
        for word in content:
            if word in badwords:
                await message.channel.send('Vamos a cuidar el lenguaje por favor')
                break
               
        
    


client = MyClient(intents=intents)
@client.event
async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hola, {member.name}, bienvenido a este servidor!'
        )

client.run(data['botToken'])

print(data['botID'])