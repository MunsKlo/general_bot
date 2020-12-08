import random
import requests
from variables import variables as var
from data import InputOutputJSON
from model import user, important_message, yt_vid, chuck_norris
from bot_logic import functions_bot


def get_inspiro_pic(parameters):
    link = "http://inspirobot.me/api?generate=true"
    f = requests.get(link)
    imgurl = f.text
    return imgurl


def get_random_number(parameters):
    try:
        return str(random.randint(1, int(parameters[1])))
    except:
        return 'Something went wrong!'


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
        var.important_messages.append(
            important_message.ImportantMessage(str(message.content), str(message.channel), str(message.author)))

        InputOutputJSON.write_json_file(var.important_messages, var.important_messages_file)

    return ''


def get_youtube(parameters):
    if len(parameters) == 4 and parameters[1] == 'add' and functions_bot.check_link(parameters[2], var.yt_link):

        if functions_bot.name_of_obj_already_exist(parameters[3], var.yt_vids):
            return 'The name already exist'

        var.yt_vids.append(yt_vid.Video(parameters[2], parameters[3]))
        InputOutputJSON.write_json_file(var.yt_vids, var.yt_vids_file)
        return 'Successfully added'

    if len(parameters) == 1 and len(var.yt_vids) > 0:
        video = var.yt_vids[random.randint(0, len(var.yt_vids) - 1)]
        return f'Name: {video.name}\n{video.link}'

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

    if len(parameters) == 1:
        for obj in var.users:
            text += obj.name + '\n'
        return text

    if parameters[1] == 'rand' and len(parameters) == 2:
        return str(var.users[random.randint(0, len(var.users) - 1)].name)

    return 'Something went wrong'


def get_commands(parameters):
    text = '```'
    for i in var.helper:
        text += f'{i} = {var.helper[i]}\n'
    return text + '```'


def get_decision(parameters):
    message = parameters[0]
    decisions_string = functions_bot.cut_parameters_from_command(str(message.content))
    decisions_list = functions_bot.cut_decisions(decisions_string)
    return f"{parameters[0].author.mention} {decisions_list[random.randint(0, len(decisions_list) - 1)]}"


def get_chuck_norris(parameters):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    json_dict = response.json()
    joke = chuck_norris.ChuckNorris(json_dict['id'], json_dict['url'], json_dict['value'])
    return f'{joke.url}\n```{joke.joke}```'


def get_giphy_gif(parameters):
    payload = {'api_key': 'AbKxlHYeNnK7yB9kDrF9gUmHMV9pbVOF', 'Content-Type': 'application/json', 'tag': ''}
    json_dict = {}

    if parameters[1] == 'random' and len(parameters) == 2:
        response = requests.get('https://api.giphy.com/v1/gifs/random', params=payload)
        json_dict = response.json()

    if parameters[1] == 'random' and len(parameters) == 3:
        payload['tag'] = parameters[2]
        response = requests.get('https://api.giphy.com/v1/gifs/random', params=payload)
        json_dict = response.json()

    return f'{json_dict["data"]["url"]}'


def get_advice(parameters):
    response = requests.get('https://api.adviceslip.com/advice')
    json_dict = response.json()
    return f'```{json_dict["slip"]["advice"]}```'


def get_cat_pic(parameters):
    response = requests.get('https://aws.random.cat/meow')
    json_dict = response.json()
    return json_dict['file']


def get_dog_pic(parameters):
    response = requests.get('https://random.dog/woof.json')
    json_dict = response.json()
    return json_dict['url']


def get_fox_pic(parameters):
    response = requests.get('https://randomfox.ca/floof/')
    json_dict = response.json()
    return json_dict['image']
