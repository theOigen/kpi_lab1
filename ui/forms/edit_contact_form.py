import npyscreen


class EditContactForm(npyscreen.ActionForm):
    def create(self):
        """
        Lifecycle function that called when form already initialized.
        Setup the form
        """
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText,
                                         name="phone_number")

    def upd_contact(self):
        """
        Function that updates contact and notify user
        about successful operation or error
        """
        if self.parentApp.contacts_manager.update_contact(self.contact) \
                is True:
            npyscreen.notify_wait("Contact has been updated! "
                                  "Contact: name: {}, phone_number: {}"
                                  .format(self.contact.get_name(),
                                          self.contact.get_phone_number()))
            self.parentApp.update_contacts_form()
            self.parentApp.switchForm("MAIN")
        else:
            npyscreen.notify_wait("Oops.. Some error occurred")

    def on_ok(self):
        """
        Function that called when form is submitted.
        Updates contact or notify user about an error
        """
        if len(self.new_name.value) == 0 and \
                len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Empty values, nothing to update here")
        else:
            new_name_len = len(self.new_name.value)
            new_phone_number_len = len(self.new_phone_number.value)
            if new_name_len != 0:
                self.contact.set_name(self.new_name.value)
            if new_phone_number_len != 0:
                self.contact.set_phone_number(self.new_phone_number.value)
            self.upd_contact()

    def on_cancel(self):
        """
        Function that called when form is canceled.
        Switches app to previous form
        """
        self.parentApp.setNextFormPrevious()

    def set_contact(self, contact):
        """
        Function that sets contact property of the form
        :param contact: Contact object
        """
        self.contact = contact
        self.new_name.value = self.contact.get_name()
        self.new_phone_number.value = self.contact.get_phone_number()

    def afterEditing(self):
        """
        Lifecycle function that called after form changed
        in both submitted or canceled cases.
        """
        self.new_name.value = ""
        self.new_phone_number.value = ""
