from src import fs
from src.contact import Contact

"""
The "ContactsManager" module

The module contains a constructor, getter and setter functions to access structure fields

"""

class ContactsManager:
    """
    Initialization
        A constructure function initialize the new object with the next fields:
            __contacts - array of Contacts which we store
            __next_id - the numerical value intended to be set as __id field of next contact we will add
        The __next_id is never decreases.
        The constructure function DOES NOT receive the arguments which correspond to each field
        By default __contacts is an empty array, __next_id is 0
        >>> contacts_manager1 = ContactsManager()
        >>> contacts_manager2 = ContactsManager()

    Adding to contacts array
        By calling an add_contact function we can append new Contact to array.
        Function accepts the new Contact, and return boolean value which means was it added or not;
        Conditions for the impossibility of adding:
            Added contact there has already been in our collection
            Added contact contained invalid data
        The validity of contact data is been checking by function validate_contact (see below)
        The ID of added item is changed by __next_id value

        >>> invalid_contact = Contact("", "", "")
        >>> valid_contact1 = Contact(100, "eugene", "+380-96-052-01-98")
        >>> valid_contact2 = Contact(100, "eugene", "+380-96-052-01-98")
        >>> contacts_manager1.add_contact(invalid_contact)
        False
        >>> valid_contact1.get_id()
        100
        >>> contacts_manager1.add_contact(valid_contact1)
        True
        >>> contacts_manager1.add_contact(valid_contact1)
        False
        >>> contacts_manager1.add_contact(valid_contact2)
        True
        >>> valid_contact1.get_id()
        0
        >>> valid_contact2.get_id()
        1
    
    Validation of Contact
        Valid Contact has
            __id:
                type:   int
                isNone: false
                value:  >=0
            __id:
                type:   str
                isNone: false
                len:  !=0
            __phone_number:
                type:   str
                isNone: false
                len:  !=0
        So validate_contact functrion will return false if
            One of fields has invalid type:
            >>> ContactsManager.validate_contact(Contact("2", "2", "2"))
            False
            >>> ContactsManager.validate_contact(Contact(2, 2, "2"))
            False
            >>> ContactsManager.validate_contact(Contact(2, "2", 2))
            False

            One of fields is None:
            >>> ContactsManager.validate_contact(Contact(None, "2", "2"))
            False
            >>> ContactsManager.validate_contact(Contact(2, None, "2"))
            False
            >>> ContactsManager.validate_contact(Contact(2, "2", None))
            False

            One of fields has invalid value or length:
            >>> ContactsManager.validate_contact(Contact(-1, "2", "2"))
            False
            >>> ContactsManager.validate_contact(Contact(2, "", "2"))
            False
            >>> ContactsManager.validate_contact(Contact(2, "2", ""))
            False

    Getting from array of Contacts
        There are two functions to get Contact from array
            get_contact_by_index - attempt to get Contact from array by its index
            get_contact_by_id - attempt to get Contact from array by its ID
        In case functions cannot find a Contact, they return None
        >>> contacts_manager1.get_contact_by_index(1) == valid_contact2
        True
        >>> contacts_manager1.get_contact_by_index(2) == None
        True
        >>> contacts_manager1.get_contact_by_id(0) == valid_contact1
        True
        >>> contacts_manager1.get_contact_by_id(3).to_dict()
        Traceback (most recent call last):
            ...
        AttributeError: 'NoneType' object has no attribute 'to_dict'

        Also we can gat all contacts by using get_contacts function
        >>> contacts_manager1.get_contacts() == [valid_contact1, valid_contact2]
        True
        >>> contacts_manager2.get_contacts() == []
        True

        We can use get_contacts function as a getter for one element
        >>> contacts_manager1.get_contacts()[0].to_dict()
        {'_id': 0, 'name': 'eugene', 'phone_number': '+380-96-052-01-98'}
        >>> contacts_manager2.get_contacts()[0].to_dict()
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
            
    Updating
        Module provide the ability to change the list of contacts
        We can change contact and put it to an array. This Contact will replace the old version of self
        If old version was not found, function returns False
        If old version was found, function returns True
        >>> valid_contact3 = Contact(valid_contact1.get_id(), valid_contact1.get_name(), valid_contact1.get_phone_number())
        >>> valid_contact4 = Contact(valid_contact1.get_id(), valid_contact1.get_name(), valid_contact1.get_phone_number())
        >>> valid_contact3.set_name("new name")

        Contact3 will replace contact1 because contacts will be equal, if their identifiers are equal
        >>> contacts_manager1.update_contact(valid_contact3)
        True
        >>> contacts_manager1.get_contacts()[0].to_dict()
        {'_id': 0, 'name': 'new name', 'phone_number': '+380-96-052-01-98'}

        If we change the id of an updated Contact, we wont be able to save chages
        >>> valid_contact1.set_id(100)
        >>> contacts_manager1.update_contact(valid_contact1)
        False

    Deleting
        There are two functions to get Contact from array
            delete_contact - attempt to get Contact from array by its index
            delete_contact_by_id - attempt to get Contact from array by its ID
        Functions return boolean value which means was an item removed or not;
        Deleting the item doesn't decreasing the __next_id value
        >>> contacts_manager1.add_contact(valid_contact4)
        True
        >>> contacts_manager1.add_contact(valid_contact1)
        True
        >>> contacts_manager1.get_next_id()
        4
        >>> len(contacts_manager1.get_contacts())
        4
        >>> contacts_manager1.delete_contact(0)
        True
        >>> contacts_manager1.get_next_id()
        4
        >>> len(contacts_manager1.get_contacts())
        3

        Deleting by ID
        >>> contacts_manager1.delete_contact_by_id(valid_contact4.get_id())
        True
        >>> contacts_manager2.delete_contact_by_id(0)
        False

        Deleting from empty array
        >>> len(contacts_manager2.get_contacts())
        0
        >>> contacts_manager2.delete_contact(0)
        False
        >>> len(contacts_manager2.get_contacts())
        0
    
    Save to file and load from file
        Module provide the ability store in ind read from file the list of contacts 
        >>> contacts_manager1.save_contacts("doctest_folder_storage/DOCTESTING_FILE__contacts_manager1__saved_data")
        True
        >>> contacts_manager2.save_contacts("doctest_folder_storage/DOCTESTING_FILE__contacts_manager2__saved_data")
        True

        After loading from a file, the addresses of objects in memory will change.
        Objects will not be equal to each other, so we will use some trick
        >>> contacts_manager3 = ContactsManager()
        >>> contacts_manager3.load_contacts("doctest_folder_storage/DOCTESTING_FILE__contacts_manager1__saved_data")
        True
        >>> contacts_manager3.get_contacts()[0].to_dict() == contacts_manager1.get_contacts()[0].to_dict()
        True

        Since the arrays are empty, they are equal anyway
        >>> contacts_manager4 = ContactsManager()
        >>> contacts_manager4.load_contacts("doctest_folder_storage/DOCTESTING_FILE__contacts_manager2__saved_data")
        True
        >>> contacts_manager4.get_contacts() == contacts_manager2.get_contacts()
        True
    """


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
        return isinstance(name, str) and name is not None and len(name) != 0 \
            and isinstance(_id, int) and _id is not None and _id >= 0 \
            and isinstance(phone_number, str)and phone_number is not None and len(phone_number) != 0

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

    def get_next_id(self):
        return self.__next_id