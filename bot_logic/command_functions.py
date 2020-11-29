import random
import requests
import json
from model import important_message
from variables import variables as var
from bot_logic import InputOutputJSON



def get_inspiro_pic(parameters):
    link = "http://inspirobot.me/api?generate=true"
    f = requests.get(link)
    imgurl = f.text
    return imgurl


def get_random_number(parameters):
    return random.randint(1, parameters[1])


def get_test(parameters):
    return "Test war erfolgreich!"


def get_yes_or_no(parameters):
    return f"{parameters[0].author.mention} {random.choice(['Ja', 'Nein'])}"


def get_all_members(parameters):
    for member in parameters[0].guild.members:
        print(member)
    return ''


def make_important_message(parameters):
    if parameters[1] == 'clear' and len(parameters) == 2:
        var.important_messages = []
        InputOutputJSON.write_json_file('PROBLEM', 'E:\Python\general_bot\data\important_messages.json')
        return 'Alle wichtigen Nachrichten wurden gelöscht'
    else:
        message = parameters[0]
        user_message = {'content': str(message.content[3:len(message.content)]), 'channel': str(message.channel), 'user': str(message.author)}
        print(user_message['user'])

        var.important_messages.append(user_message)
        InputOutputJSON.write_json_file(var.important_messages, 'E:\Python\general_bot\data\important_messages.json')
    return ''

