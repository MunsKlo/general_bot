import random
import requests
from variables import variables as var
from data import InputOutputJSON
from model import  user, important_message, yt_vid
from bot_logic import functions_bot


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
        InputOutputJSON.write_json_file([], var.important_messages_file, True)
        return 'Alle wichtigen Nachrichten wurden gelöscht'

    elif parameters[1] == 'print' and len(parameters) == 2:
        text = ''
        for obj in var.important_messages:
            text += f'{obj.user} schrieb: "{obj.message}" in {obj.channel}\n'
        if text == '':
            text = 'Keine Nachrichten vorhanden'
        return text

    else:
        message = parameters[0]
        var.important_messages.append(important_message.ImportantMessage(str(message.content), str(message.channel), str(message.author)))

        InputOutputJSON.write_json_file(var.important_messages, var.important_messages_file)

    return ''


def get_youtube(parameters):

    if len(parameters) == 4 and parameters[1] == 'add' and functions_bot.check_link(parameters[2] ,var.yt_link):
        var.yt_vids.append(yt_vid.Video(parameters[2], parameters[3]))
        InputOutputJSON.write_json_file(var.yt_vids, var.yt_vids_file)
        return 'Erfolgreich hinzugefügt'

    if len(parameters) == 1 and len(var.yt_vids) > 0:
        return var.yt_vids[random.randint(0, len(var.yt_vids) - 1)].link

    if len(parameters) == 2 and parameters[1] == 'list':
        names = ''
        for obj in var.yt_vids:
            names += f'{obj.name}\n'
        return names

    if len(parameters) == 2:
        for obj in var.yt_vids:
            if parameters[1] == obj.name:
                return obj.link
        return "Link not founded"

    else:
        return 'Something went wrong!'


def get_users(parameters):
    text = ''
    for user in var.users:
        text += user.name + '\n'
    return text


def get_commands(parameters):
    text = '```'
    for i in var.helper:
        text += f'{i} = {var.helper[i]}\n'
    return text + '```'


