import json


def get_contacts():
    file = open("data.json", "r")
    json_object = json.load(file)
    file.close()
    return json_object


def get_contact_by_index(contact_index):
    return get_contacts()["contacts"][contact_index]


def save_contacts(src_object):
    file = open("data.json", "w")
    json.dump(src_object, file, indent=4, sort_keys=True)
    file.close()


def create_contact(name, phone_number):
    new_contact = {
        "id": -1,
        "name": name,
        "phone_number": phone_number
    }
    dict_obj = get_contacts()
    new_contact["id"] = dict_obj["next_id"]
    dict_obj["next_id"] += 1
    dict_obj["contacts"].append(new_contact)
    save_contacts(dict_obj)
    return new_contact


def delete_contact(contact_index):
    dict_obj = get_contacts()
    contacts = dict_obj["contacts"]
    contacts.pop(contact_index)
    save_contacts(dict_obj)
