important_messages = []

users = []

yt_vids = []

users_file = 'users.json'
important_messages_file = 'important_messages.json'
yt_vids_file = 'yt_vids.json'
msgs_file = 'msgs.json'

#CheckStates
path_data = ''

yt_link = 'https://www.youtube.com/watch?'

helper = {
    ".inspiro": "Get a random picture from the inspiro-bot",
    ".number <number>": "Get a random number ",
    ".test": "Test the bot",
    ".jn <question>": "Get a yes or no answer to a question",
    ".members": "Coming soon",
    ".users": "Get a list of all users",
    ".users rand": "Get an user randomly",
    ".vid": "Get a random video",
    ".vid add <link> <name>": "Add a video with a name",
    ".vid list": "List all names of videos",
    ".vid <name>": "Get a video with a name",
    ".help": "Get all commands",
    ".@": "Create a important message",
    ".@ clear": "Delete all important messages",
    ".advice": "Give you a random advice",
    ".decision <decision1> <decision2> <decision n>": "Take randomly a decision",
    ".giphy random": "Give you a absolute random gif",
    ".giphy random <tag>": "Give you a random gif from a specific topic",
    ".chucknorris": "Get a Chuck Norris joke",
}

msgs = {}
