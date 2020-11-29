import bot_logic.variables


def right_channel(channel):
    return channel in bot_logic.variables.allowed_channels


def get_command_from_content(text):

    new_text = ''

    for letter in text:
        if letter == ' ':
            break
        new_text += letter
    return new_text[1:len(new_text)]


def get_parameter_list(text, message):
    parameter_list = [message]

    if ' ' in text:
        parameters = cut_parameters_from_command(text)
        parameter_list += fill_parameters_in_list(parameters)

    return parameter_list


def cut_parameters_from_command(text):
    new_text = ''
    for index in range(len(text)):
        if text[index] == ' ':
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

