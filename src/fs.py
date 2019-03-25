import json


def read_json_file(file_name):
    file = open(file_name, "r")
    obj = json.load(file)
    file.close()
    return obj


def save_json_file(file_name, src_object):
    file = open(file_name, "w")
    json.dump(src_object, file, indent=4, sort_keys=True)
    file.close()

