import json


def write_json_file(obj, file_path):
    json_string = json.dumps(obj)
    file = open(file_path, 'w')
    file.write(json_string)
    file.close()


def read_json_file(file_path):
    file = open(file_path, 'r')
    json_string = file.readlines()
    file.close()
    print(json_string)
    return json_string
