from src import fs


def get_contacts():
    return fs.read_json_file(file_name="data.json")


def get_contact_by_index(contact_index):
    return get_contacts()["contacts"][contact_index]


def get_contact_by_id(contact_id):
    contacts = get_contacts()["contacts"]
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact


def save_contacts(src_object):
    fs.save_json_file("data.json", src_object)


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


def update_contact(updated):
    dict_obj = get_contacts()
    contacts = dict_obj["contacts"]
    for index, contact in enumerate(contacts):
        if contact["id"] == updated["id"]:
            contacts[index] = updated
    save_contacts(dict_obj)


def delete_contact(contact_index):
    dict_obj = get_contacts()
    contacts = dict_obj["contacts"]
    contacts.pop(contact_index)
    save_contacts(dict_obj)

