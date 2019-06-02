import json


def read_json_file(file_name):
    """
    Function that reads a file
    :param file_name: file to read
    :return: dictionary with array of contacts and next_id field
    """
    try:
        file = open(file_name, "r")
        obj = json.load(file)
        file.close()
        return obj
    except (OSError, IOError):
        return {
            "contacts": [],
            "next_id": 0
        }


def save_json_file(file_name, src_object):
    """
    Function that writes data to a file
    :param file_name: file to write
    :param src_object: dictionary with array of contacts
    and next_id field to save
    """
    file = open(file_name, "w")
    json.dump(src_object, file, indent=4, sort_keys=True)
    file.close()
