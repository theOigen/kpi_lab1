from unittest import TestCase
from src import contacts


class TestContacts(TestCase):

    def test_get_contacts_correct(self):
        file_name = "../data_files/test_file_1.json"
        conts = {
            "contacts": [
                {
                    "name": "User1",
                    "phone_number": "123-322-32-32"
                }
            ]
        }
        contacts.save_contacts(conts, file_name)
        another_conts = contacts.get_contacts(file_name)
        self.assertEqual(contacts.compare_contacts(conts["contacts"], another_conts["contacts"]), True,
                         'Contacts should be similliar')

    def test_get_contacts_incorrect(self):
        file_name = "../data_files/test_file_1.json"
        conts = {
            "contacts": [
                {
                    "name": "user2",
                    "phone_number": ""
                }
            ]
        }
        another_conts = contacts.get_contacts(file_name)
        self.assertEqual(contacts.compare_contacts(conts["contacts"], another_conts["contacts"]), False,
                         'Contacts should not be similliar')

