import random
import requests

allowed_channels = ("general_bot_testing", "senseless-gelaber")


def right_channel(channel):
    return channel in allowed_channels


def get_inspiro_pic(message):
    link = "http://inspirobot.me/api?generate=true"
    f = requests.get(link)
    imgurl = f.text
    return imgurl


def get_random_number(message, numb):
    return random.randint(1, numb)


def get_test(message):
    return "Test war erfolgreich!"


def get_yes_or_no(message):
    return f"{message.author.mention} {random.choice(['Ja', 'Nein'])}"


def get_all_members(message):
    for member in message.guild.members:
        print(member)
    return ""
