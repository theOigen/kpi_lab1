from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
from src.contact import Contact
from src.contacts import ContactsManager

app = Flask(__name__, static_url_path="")
api = Api(app)


class ContactApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, default="None",
                                   location='json')
        self.reqparse.add_argument('phone_number', type=str, default="None",
                                   location='json')
        self.contacts_manager = ContactsManager()
        self.data_path = "data.json"
        super(ContactApi, self).__init__()

    def get(self, id):
        self.contacts_manager.load_contacts(self.data_path)
        requested_contact = self.contacts_manager.get_contact_by_id(id)
        if requested_contact is None:
            abort(404)
        return {'contact': requested_contact.to_dict()}

    def put(self, id):
        self.contacts_manager.load_contacts(self.data_path)
        args = self.reqparse.parse_args()
        updated_contact = Contact(id, args['name'], args['phone_number'])
        result = self.contacts_manager.update_contact(updated_contact)
        self.contacts_manager.save_contacts(self.data_path)
        return {'result': result}

    def delete(self, id):
        self.contacts_manager.load_contacts(self.data_path)
        result = self.contacts_manager.delete_contact_by_id(id)
        self.contacts_manager.save_contacts(self.data_path)
        return {'result': result}


class ContactManagerAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   location='json')
        self.reqparse.add_argument('phone_number', type=str, required=True,
                                   location='json')
        self.contacts_manager = ContactsManager()
        self.data_path = "data.json"
        super(ContactManagerAPI, self).__init__()

    def get(self):
        self.contacts_manager.load_contacts(self.data_path)
        raw_list = self.contacts_manager.get_contacts()
        map_iterator = map(lambda contact: contact.to_dict(), raw_list)
        contact_list = list(map_iterator)
        return {'contacts': contact_list}

    def post(self):
        args = self.reqparse.parse_args()
        self.contacts_manager.load_contacts(self.data_path)
        created_contact = Contact(0, args['name'], args['phone_number'])
        result = self.contacts_manager.add_contact(created_contact)
        self.contacts_manager.save_contacts(self.data_path)
        if result is True:
            return {'contact': created_contact.to_dict()}
        return {'error': 'Invalid arguments'}, 400


api.add_resource(ContactManagerAPI, '/api/v1.0/contacts', endpoint='contacts')
api.add_resource(ContactApi, '/api/v1.0/contacts/<int:id>', endpoint='contact')

if __name__ == "__main__":
    server = app
    server.run(debug=True)
