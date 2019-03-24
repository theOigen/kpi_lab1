import npyscreen
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


def delete_contact(id):
    dict_obj = get_contacts()
    contacts = list(dict_obj["contacts"])


class ConsoleUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm, name="Main Menu")
        self.addForm("GetCont", AllContactsForm, name="All Contacts")
        self.addForm("CreateCont", CreateContactForm, name="Create Contact")
        self.addForm("EditCont", EditContactForm, name="Edit Contact")

    def update_contacts_form(self):
        self.getForm("GetCont").upd()


class WelcomeForm(npyscreen.FormWithMenus):
    def all_contacts(self):
        self.parentApp.switchForm("GetCont")

    def create_contact(self):
        self.parentApp.switchForm("CreateCont")

    def exit(self):
        self.exit_editing()
        self.parentApp.setNextForm(None)

    def create(self):
        self.menu = self.new_menu(name="Main Menu")
        self.options = ["Get contacts", "Create contact", "Quit"]
        self.menu.addItem(self.options[0], self.all_contacts)
        self.menu.addItem(self.options[1], self.create_contact)
        self.menu.addItem(self.options[2], self.exit)


class AllContactsForm(npyscreen.ActionFormV2):
    def upd(self):
        self.choosen_contact.values = get_contacts()["contacts"]
        self.choosen_contact.value = None
        self.my_choice.value = None

    def create(self):
        self.choosen_contact = self.add(npyscreen.TitleSelectOne, max_height=4, name="Choose any contact",
                                        values=get_contacts()["contacts"], value=None, scroll_exit=True)
        self.menu = ["Edit contact", "Delete contact"]
        self.my_choice = self.add(npyscreen.TitleSelectOne, max_height=3, name="What you want to do with contact?",
                                  values=self.menu, scroll_exit=True)

    def on_ok(self):
        if len(self.my_choice.value) < 1 or len(self.choosen_contact.value) < 1:
            npyscreen.notify_wait("Please, to submit the form you must choose the contact and the action!",
                                  title="Error occurred")
        elif self.my_choice.get_selected_objects()[0] == self.menu[0]:
            self.parentApp.getForm("EditCont").setContact(self.choosen_contact.value[0])
            self.parentApp.switchForm("EditCont")
        # elif self.my_choice.get_selected_objects()[0] == self.menu[1]:
        #     todo

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()


class CreateContactForm(npyscreen.ActionForm):
    def create(self):
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText, name="phone_number")

    def on_ok(self):
        if len(self.new_name.value) == 0 or len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Some of values is empty, cannot create contact. Try again please.",
                                  title="Error occurred")
        else:
            new_contact = create_contact(self.new_name.value, self.new_phone_number.value)
            npyscreen.notify_wait("Contact has been created! New contact: {}".format(new_contact))
            self.parentApp.update_contacts_form()
            self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()

    def afterEditing(self):
        self.new_name.value = ""
        self.new_phone_number.value = ""


class EditContactForm(npyscreen.ActionForm):
    def create(self):
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText, name="phone_number")

    def on_ok(self):
        if len(self.new_name.value) == 0 and len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Empty values, nothing to update here")
        elif len(self.new_name.value) != 0 and len(self.new_phone_number.value) != 0:
            self.contact["phone_number"] = self.new_phone_number.value
            self.contact["name"] = self.new_name.value
            dict_obj = get_contacts()
            contacts = dict_obj["contacts"]
            contacts[self.contact_index] = self.contact
            save_contacts(dict_obj)
            npyscreen.notify_wait("Contact has been updated! New contact: {}".format(self.contact))
            self.parentApp.update_contacts_form()
            self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()

    def setContact(self, contact_index):
        self.contact_index = contact_index
        self.contact = get_contact_by_index(contact_index)

    def afterEditing(self):
        self.new_name.value = ""
        self.new_phone_number.value = ""


if __name__ == "__main__":
    UI = ConsoleUI()
    UI.run()
