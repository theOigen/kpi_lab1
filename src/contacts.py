from src import fs


def get_contacts(file_name="data.json"):
    return fs.read_json_file(file_name)


def compare_contacts(conts_1, conts_2):
    for index, val in enumerate(conts_1):
        if val["name"] != conts_2[index]["name"] \
                    or val["phone_number"] != conts_2[index]["phone_number"]:
            return False
    return True


def get_contact_by_index(contact_index, file_name="data.json"):
    return get_contacts(file_name)["contacts"][contact_index]


def get_contact_by_id(contact_id, file_name="data.json"):
    contacts = get_contacts(file_name)["contacts"]
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact


def save_contacts(src_object, file_name="data.json"):
    fs.save_json_file(file_name, src_object)


def create_contact(name, phone_number, file_name="data.json"):
    new_contact = {
        "id": -1,
        "name": name,
        "phone_number": phone_number
    }
    dict_obj = get_contacts(file_name)
    new_contact["id"] = dict_obj["next_id"]
    dict_obj["next_id"] += 1
    dict_obj["contacts"].append(new_contact)
    save_contacts(dict_obj, file_name)
    return new_contact


def update_contact(updated, file_name="data.json"):
    dict_obj = get_contacts(file_name)
    contacts = dict_obj["contacts"]
    for index, contact in enumerate(contacts):
        if contact["id"] == updated["id"]:
            contacts[index] = updated
    save_contacts(dict_obj, file_name)


def delete_contact(contact_index, file_name="data.json"):
    dict_obj = get_contacts(file_name)
    contacts = dict_obj["contacts"]
    contacts.pop(contact_index)
    save_contacts(dict_obj, file_name)

