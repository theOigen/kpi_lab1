import npyscreen


class EditContactForm(npyscreen.ActionForm):
    def create(self):
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText,
                                         name="phone_number")

    def upd_contact(self):
        if self.parentApp.contacts_manager.update_contact(self.contact) \
                is True:
            npyscreen.notify_wait("Contact has been updated! "
                                  "Contact: name: {}, phone_number: {}"
                                  .format(self.contact.get_name(),
                                          self.contact.get_phone_number()))
        else:
            npyscreen.notify_wait("Oops.. Some error occurred")
        self.parentApp.update_contacts_form()
        self.parentApp.switchForm("MAIN")

    def on_ok(self):
        if len(self.new_name.value) == 0 and \
                len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Empty values, nothing to update here")
        else:
            if len(self.new_name.value) != 0 and \
                    len(self.new_phone_number.value) != 0:
                self.contact.set_phone_number(self.new_phone_number.value)
                self.contact.set_name(self.new_name.value)
            elif len(self.new_name.value) != 0:
                self.contact.set_name(self.new_name.value)
            elif len(self.new_phone_number.value) != 0:
                self.contact.set_phone_number(self.new_phone_number.value)
            self.upd_contact()

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()

    def set_contact(self, contact):
        self.contact = contact
        self.new_name.value = self.contact.get_name()
        self.new_phone_number.value = self.contact.get_phone_number()

    def afterEditing(self):
        self.new_name.value = ""
        self.new_phone_number.value = ""
