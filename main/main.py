import discord
import os
import commandHandler.commandHandler
import bot_logic.admin_logic
import json

token = os.environ.get('General_Bot')

comHandler = commandHandler.commandHandler.commandHandler

functions = commandHandler.commandHandler.functions

list_of_members = []


class MyClient(discord.Client):

    # LogIn
    async def on_ready(self):
        print("Ich bin eingeloggt!")
        guild = bot_logic.admin_logic.get_right_guild(client.guilds)# client.guilds[1].members
        print(guild.members)

    # MessageSend
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('.') and functions['right_channel'](message.channel.name):
            bot_message = ''
            result = ''
            command = message.content[1:len(message.content)]

            if command in comHandler:
                function = comHandler[command]
                result = function(message)

            bot_message = result
            await message.channel.send(bot_message)


# Client erstellt und mit dem Bot verbunden
client = MyClient()
client.run(token)
