"""
The "Contact" module
The module contains a constructor, getter and setter functions to access
structure fields
Initialization
    A constructure function initialize the new object with the next fields:
        __id - the identifier of new object
        __name - the name of owner of the phone number we want to store
        __phone_numder - the telephone number of person whose data we want
        to store
    The constructure function receive the arguments which correspond
    to each field

    >>> contact1 = Contact(0, "eugene", "+380-96-052-01-98")
    >>> contact2 = Contact(-1111*10, "", "")

Getter and setter function for access with a "__id" field of a Contact
    By calling a get_id we can receive a identifier of an object
    >>> contact1.get_id()
    0
    >>> contact2.get_id()
    -11110

    By caling a set_id we can change inentifire of an object
    >>> contact1.set_id("@@@")
    >>> contact1.get_id()
    '@@@'

    We also can set the current _id of an object or the _id
    of another object
    >>> contact2.set_id(contact1.get_id())
    >>> contact2.get_id()
    '@@@'

    But we cannot miss the argument in setter-function
    >>> contact2.set_id()
    Traceback (most recent call last):
        ...
    TypeError: set_id() missing 1 required positional argument: '_id'

Getter and setter function for access with a "__name" field of a Contact
    By calling a get_name we can receive a name field of an object
    >>> contact1.get_name()
    'eugene'
    >>> contact2.get_name()
    ''

    By caling a set_name we can change name field of an object
    >>> contact1.set_name("@@@")
    >>> contact1.get_name()
    '@@@'

    We also can set the current name of an object or the
    name of another object
    >>> contact2.set_name(contact1.get_name())
    >>> contact2.get_name()
    '@@@'

Getter and setter function for access with a "__phone_numder" field
of a Contact
    By calling a get_phone_number we can receive a phone numder field
    of an object
    >>> contact1.get_phone_number()
    '+380-96-052-01-98'
    >>> contact2.get_phone_number()
    ''

    By caling a set_phone_number we can change phone number field
    of an object
    >>> contact1.set_phone_number("@@@")
    >>> contact1.get_phone_number()
    '@@@'

    We also can set the current phone of an object or the phone
    of another object
    >>> contact2.set_phone_number(contact1.get_phone_number())
    >>> contact2.get_phone_number()
    '@@@'

Creation the Dictionary
The Dictionary contains the names of fields as the key
    and their values as own values
    The Dictionary are created by calling a to_dict functrion
    >>> contact1.to_dict()
    {'_id': '@@@', 'name': '@@@', 'phone_number': '@@@'}
    >>> contact2.to_dict()
    {'_id': '@@@', 'name': '@@@', 'phone_number': '@@@'}
"""


class Contact:
    def __init__(self, _id, name, phone_number):
        """
        Initializator of an object
        :param _id: unique integer identifier
        :param name: string that specify the name
        :param phone_number: string that specify the phone number
        """
        self.__id = _id
        self.__name = name
        self.__phone_number = phone_number

    def get_name(self):
        """
        :return: name of a contact
        """
        return self.__name

    def set_name(self, name):
        """
        Set the __name property
        :param name: new name for contact
        """
        self.__name = name

    def set_phone_number(self, phone_number):
        """
        Set the __phone_number property
        :param phone_number: new phone number for contact
        """
        self.__phone_number = phone_number

    def get_phone_number(self):
        """
        :return: return phone number of a contact
        """
        return self.__phone_number

    def set_id(self, _id):
        """
        Set the __id property
        :param _id: unique integer identifier
        """
        self.__id = _id

    def get_id(self):
        """
        :return: id of a contact
        """
        return self.__id

    def to_dict(self):
        """
        Function that converts Contact object to dictionary,
        used for serialize the object
        :return: dictionary with _id, name and phone_number fields
        """
        return {
            "_id": self.__id,
            "name": self.__name,
            "phone_number": self.__phone_number
        }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
