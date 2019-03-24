import npyscreen
import contacts


class EditContactForm(npyscreen.ActionForm):
    def create(self):
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText, name="phone_number")

    def upd_contact(self):
        dict_obj = contacts.get_contacts()
        _contacts = dict_obj["contacts"]
        _contacts[self.contact_index] = self.contact
        contacts.save_contacts(dict_obj)
        npyscreen.notify_wait("Contact has been updated! New contact: {}".format(self.contact))
        self.parentApp.update_contacts_form()
        self.parentApp.switchForm("MAIN")

    def on_ok(self):
        if len(self.new_name.value) == 0 and len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Empty values, nothing to update here")
        else:
            if len(self.new_name.value) != 0 and len(self.new_phone_number.value) != 0:
                self.contact["phone_number"] = self.new_phone_number.value
                self.contact["name"] = self.new_name.value
            elif len(self.new_name.value) != 0:
                self.contact["name"] = self.new_name.value
            elif len(self.new_phone_number.value) != 0:
                self.contact["phone_number"] = self.new_phone_number.value
            self.upd_contact()

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()

    def setContact(self, contact_index):
        self.contact_index = contact_index
        self.contact = contacts.get_contact_by_index(contact_index)

    def afterEditing(self):
        self.new_name.value = ""
        self.new_phone_number.value = ""
