import bot_logic.variables
from model import user, important_message, yt_vid


def right_channel(channel):
    return channel in bot_logic.variables.allowed_channels


def get_command_from_content(text):

    new_text = ''

    for letter in text:
        if letter == ' ' or letter == '\n':
            break
        new_text += letter
    return new_text[1:len(new_text)]


def get_parameter_list(text, message):
    parameter_list = [message]

    if ' ' in text or '\n' in text:
        parameters = cut_parameters_from_command(text)
        parameter_list += fill_parameters_in_list(parameters)

    return parameter_list


def cut_parameters_from_command(text):
    new_text = ''
    for index in range(len(text)):
        if text[index] == ' ' or text[index] == '\n':
            new_text = text[index + 1:len(text)]
            break
    return new_text


def fill_parameters_in_list(parameters):
    parameter = ''
    parameter_list = []
    print(parameters)
    for letter in parameters:
        if letter == ' ':
            parameter_list.append(parameter)
            parameter = ''
        else:
            parameter += letter
    parameter_list.append(parameter)
    return parameter_list


def check_if_user_register(name, list):
    user_exist = False
    for member in list:
        if name == member.name:
            user_exist = True
            break

    return user_exist


def create_user(name):
    return user.User(name)


def convert_dict_in_obj_list(list_obj, type_obj):

    new_list = []

    if type_obj == 'user':
        for obj in list_obj:
            new_list.append(user.User(obj['name']))

    if type_obj == 'important_message':
        for obj in list_obj:
            new_list.append(important_message.ImportantMessage(obj['message'], obj['channel'], obj['user']))

    if type_obj == 'yt_vid':
        for obj in list_obj:
            new_list.append(yt_vid.Video(obj['link'], obj['name']))

    return new_list


def check_link(link, yt_link):
    for i in range(len(yt_link)):
        if link[i] != yt_link[i]:
            return False
    return True


def name_of_obj_already_exist(name, obj_list):
    for obj in obj_list:
        if obj.name == name:
            return True
    return False


def cut_decisions(decisions):
    if not len(decisions):
        return 'No decisions'

    decision = ''
    decision_list = []
    string_with_whitespace = False
    for index in range(len(decisions)):
        if decisions[index] == '"' and not string_with_whitespace:
            string_with_whitespace = True
            continue

        if decisions[index] == '"' and string_with_whitespace:
            string_with_whitespace = False
            decision_list.append(decision)
            decision = ''
            continue

        if decisions[index] == ' ' and not string_with_whitespace and len(decision):
            decision_list.append(decision)
            decision = ''

        elif decisions[index] == ' ' and not string_with_whitespace:
            continue

        else:
            decision += decisions[index]

    if len(decision):
        decision_list.append(decision)

    return decision_list
