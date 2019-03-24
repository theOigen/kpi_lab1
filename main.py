import npyscreen
import json


class ConsoleUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", FirstForm, name="Main Menu")
        self.addForm("GetCont", SecondForm, name="All Contacts")
        self.addForm("EditCont", EditForm, name="Edit Contact")


class FirstForm(npyscreen.FormWithMenus):
    def all_contacts(self):
        self.parentApp.switchForm("GetCont")

    def create(self):
        self.menu = self.new_menu(name="Main Menu")
        self.options = ["Get contacts", "Create contact", "Update Contact", "Delete Contact"]
        self.menu.addItem(self.options[0], self.all_contacts)
        self.menu.addItem(self.options[1])
        self.menu.addItem(self.options[2])
        self.menu.addItem(self.options[3])


def get_contacts():
    file = open("data.json", "r")
    contacts = json.load(file)["contacts"]
    file.close()
    return contacts


def save_contacts(contacts):
    file = open("data.json", "w")
    json.dump({"contacts": contacts}, file, indent=4)
    file.close()


class SecondForm(npyscreen.ActionFormV2):
    def upd(self):
        self.choosen_contact.values = get_contacts()
        self.choosen_contact.value = -len(self.choosen_contact.values)
        self.my_choice.value = -2

    def create(self):
        self.choosen_contact = self.add(npyscreen.TitleSelectOne, max_height=4, name="Choose any contact",
                                        values=get_contacts(), value=None, scroll_exit=True)
        self.menu = ["Edit contact", "Delete contact"]
        self.my_choice = self.add(npyscreen.TitleSelectOne, max_height=3, name="What you want to do with contact?",
                                  values=self.menu, scroll_exit=True)

    def on_ok(self):
        if len(self.my_choice.value) < 1 or len(self.choosen_contact.value) < 1:
            npyscreen.notify_wait("Please, to submit the form you must choose the contact and the action!",
                                  title="Error occurred")
        else:
            self.parentApp.getForm("EditCont").setContact(self.choosen_contact.value[0])
            self.parentApp.switchForm("EditCont")

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()


class EditForm(npyscreen.ActionForm):
    def create(self):
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText, name="phone_number")

    def on_ok(self):
        if len(self.new_name.value) == 0 and len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Empty values, nothing to update here")
        elif len(self.new_name.value) != 0 and len(self.new_phone_number.value) != 0:
            self.contact["phone_number"] = self.new_phone_number.value
            self.contact["name"] = self.new_name.value
            contacts = get_contacts()
            contacts[self.contact_index] = self.contact
            save_contacts(contacts)
            npyscreen.notify_wait("Contact has been updated! New contact: {}".format(self.contact))
            self.parentApp.getForm("GetCont").upd()
            self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()

    def setContact(self, contact_index):
        self.contact_index = contact_index
        self.contact = get_contacts()[contact_index]

    def afterEditing(self):
        self.new_name.value = ""
        self.new_phone_number.value = ""


if __name__ == "__main__":
    UI = ConsoleUI()
    UI.run()
    