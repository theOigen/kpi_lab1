from src import fs
from src.contact import Contact


class ContactsManager:
    def __init__(self):
        self.__contacts = []
        self.__next_id = 0

    def get_contacts(self):
        return self.__contacts

    def get_contact_by_index(self, index):
        if index >= len(self.__contacts) \
                or abs(index) > len(self.__contacts):
            return None
        return self.__contacts[index]

    def get_contact_by_id(self, _id):
        for contact in self.__contacts:
            if contact.get_id() == _id:
                return contact
        return None

    @staticmethod
    def validate_contact(contact):
        name = contact.get_name()
        _id = contact.get_id()
        phone_number = contact.get_phone_number()
        return name is not None and len(name) != 0 and _id is not None \
            and _id >= 0 and phone_number is not None and len(phone_number) != 0

    def add_contact(self, contact):
        if ContactsManager.validate_contact(contact) is True and self.__contacts.count(contact) == 0:
            contact.set_id(self.__next_id)
            self.__contacts.append(contact)
            self.__next_id += 1
            return True
        return False

    def update_contact(self, updated):
        if ContactsManager.validate_contact(updated) is False:
            return False
        for index, contact in enumerate(self.__contacts):
            if contact.get_id() == updated.get_id():
                self.__contacts[index] = updated
                return True
        return False
    

    def delete_contact(self, contact_index):
        if contact_index >= len(self.__contacts) \
                or abs(contact_index) > len(self.__contacts):
            return False
        self.__contacts.pop(contact_index)
        return True
    def delete_contact_by_id(self, id):
        contact = [contact for contact in self.__contacts if contact.get_id() == id]
        if len(contact) == 0:
            return False
        self.__contacts.remove(contact[0])
        return True

    def save_contacts(self, file_name="data.json"):
        fs.save_json_file(file_name, {
            "contacts": [contact.to_dict() for contact in self.__contacts],
            "next_id": self.__next_id
        })
        return True

    def load_contacts(self, file_name="data.json"):
        contacts_dict = fs.read_json_file(file_name)
        contacts_array = contacts_dict["contacts"]
        for contact_dict in contacts_array:
            self.__contacts.append(Contact(contact_dict["_id"], contact_dict["name"],
                                           contact_dict["phone_number"]))
        self.__next_id = contacts_dict["next_id"]
        return True
