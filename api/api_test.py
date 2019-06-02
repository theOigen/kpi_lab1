import requests


def get_contact(contact_id):
    url = 'http://127.0.0.1:5000/api/v1.0/contacts/{:d}'.format(contact_id)
    return requests.get(url)


def get_contacts_list():
    url = 'http://127.0.0.1:5000/api/v1.0/contacts'
    return requests.get(url)


def post_contact(post_data):
    url = 'http://127.0.0.1:5000/api/v1.0/contacts'
    return requests.post(url, json=post_data)


def put_contact(contact_id, post_data):
    url = 'http://127.0.0.1:5000/api/v1.0/contacts/{:d}'.format(contact_id)
    return requests.put(url, json=post_data)


def delete_contact(contact_id):
    url = 'http://127.0.0.1:5000/api/v1.0/contacts/{:d}'.format(contact_id)
    return requests.delete(url)


class TestClass(object):
    def test_get_list(self):
        response = get_contacts_list()
        assert response.ok

    def test_get_valid_existing_id(self):
        response = get_contact(0)
        assert response.ok

    def test_get_valid_not_existing_id(self):
        response = get_contact(10000)
        assert response.ok is False

    def test_post_new_and_get_it(self):
        response = post_contact({'name': 'test_user', 'phone_number': '1111'})
        new_id = response.json()['contact']['_id']
        response = get_contact(new_id)
        created_contact = response.json()['contact']
        print(created_contact)
        assert response.ok
        assert created_contact['name'] == 'test_user'
        assert created_contact['phone_number'] == '1111'

    def test_post_invalid(self):
        response = post_contact({})
        assert response.ok is False

    def test_update_new_and_get_it(self):
        response = post_contact({'name': 'test_user', 'phone_number': '1111'})
        new_id = response.json()['contact']['_id']
        new_id = int(new_id)
        new_contact = {'name': 'updated_contact', 'phone_number': '0000'}
        response = put_contact(new_id, new_contact)
        updated_result = response.json()['result']
        print(updated_result)
        response = get_contact(new_id)
        updated_contact = response.json()['contact']
        assert response.ok
        assert updated_result
        assert updated_contact['name'] == 'updated_contact'
        assert updated_contact['phone_number'] == '0000'

    def test_update_not_existing(self):
        new_contact = {'name': 'updated_contact', 'phone_number': '0000'}
        response = put_contact(1000, new_contact)
        updated_result = response.json()['result']
        print(updated_result)
        assert updated_result is False

    def test_delete_new(self):
        response = post_contact({'name': 'test_user', 'phone_number': '1111'})
        new_id = response.json()['contact']['_id']
        new_id = int(new_id)
        response = delete_contact(new_id)
        delete_result = response.json()['result']
        print(delete_result)
        response_on_deleted = get_contact(new_id)
        assert response_on_deleted.ok is False
        assert response.ok
        assert delete_result

    def test_delete_not_existing(self):
        response = delete_contact(1000)
        delete_result = response.json()['result']
        print(delete_result)
        assert delete_result is False
