class Contact():
    def __init__(self, _id, name, phone_number):
        self.__id = _id
        self.__name = name
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def set_id(self, _id):
        self.__id = _id

    def get_id(self):
        return self.__id

    def to_dict(self):
        return {
            "_id": self.__id,
            "name": self.__name,
            "phone_number": self.__phone_number
        }
