import npyscreen
from src import contacts


class CreateContactForm(npyscreen.ActionForm):
    def create(self):
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText, name="phone_number")

    def on_ok(self):
        if len(self.new_name.value) == 0 or len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Some of values is empty, cannot create contact. Try again please.",
                                  title="Error occurred")
        else:
            new_contact = contacts.create_contact(self.new_name.value, self.new_phone_number.value)
            npyscreen.notify_wait("Contact has been created! New contact: {}".format(new_contact))
            self.parentApp.update_contacts_form()
            self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()

    def afterEditing(self):
        self.new_name.value = ""
        self.new_phone_number.value = ""
