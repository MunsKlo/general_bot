import discord
import os
import commandHandler.commandHandler
from bot_logic import admin_logic, functions_bot, InputOutputJSON
from variables import variables as var

token = os.environ.get('General_Bot')

comHandler = commandHandler.commandHandler.commandHandler

list_of_members = []


class MyClient(discord.Client):

    # LogIn
    async def on_ready(self):
        print("Ich bin eingeloggt!")
        guild = admin_logic.get_right_guild(client.guilds)# client.guilds[1].members

        important_messages_content = InputOutputJSON.read_json_file('E:\Python\general_bot\data\important_messages.json')
        var.important_messages = important_messages_content

    # MessageSend
    async def on_message(self, message):
        if message.author == client.user:
            return
        if functions_bot.right_channel(str(message.channel)) and message.content.startswith('.'):
            print(functions_bot.right_channel(str(message.channel)))
            bot_message = ''
            result = ''

            command = functions_bot.get_command_from_content(message.content)
            parameter_list = functions_bot.get_parameter_list(message.content, message)
            # print(parameter_list)

            if command in comHandler:
                function = comHandler[command]
                result = function(parameter_list)

            bot_message = result
            if len(bot_message):
                await message.channel.send(bot_message)


# Client erstellt und mit dem Bot verbunden
client = MyClient()
client.run(token)
