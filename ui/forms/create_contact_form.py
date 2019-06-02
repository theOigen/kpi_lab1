import npyscreen
from src.contact import Contact


def notify_about_success(new_contact):
    """
    Notifies user about successful creating of a contact
    :param new_contact: valid Contact object
    """
    npyscreen.notify_wait("Contact has been created! "
                          "New contact: "
                          "id: {}, name: {}, phone_number: {}"
                          .format(new_contact.get_id(),
                                  new_contact.get_name(),
                                  new_contact.get_phone_number()))


class CreateContactForm(npyscreen.ActionForm):
    def create(self):
        """
        Lifecycle function that called when form already initialized.
        Setup the form
        """
        self.new_name = self.add(npyscreen.TitleText, name="name")
        self.new_phone_number = self.add(npyscreen.TitleText,
                                         name="phone_number")

    def on_ok(self):
        """
        Function that called when form is submitted.
        Creates contact, adds him to contacts array via contacts manager
        and switches app to MAIN form if everything is valid.
        Else notifies user about an error.
        """
        if len(self.new_name.value) == 0 or \
                len(self.new_phone_number.value) == 0:
            npyscreen.notify_wait("Some of values is empty, "
                                  "cannot create contact. Try again please.",
                                  title="Error occurred")
        else:
            new_contact = Contact(0, self.new_name.value,
                                  self.new_phone_number.value)
            if self.parentApp.contacts_manager.add_contact(new_contact) \
                    is True:
                notify_about_success(new_contact)
                self.parentApp.update_contacts_form()
                self.parentApp.switchForm("MAIN")
            else:
                npyscreen.notify_wait("Oops.. Some error occurred...",
                                      title="Error occurred")

    def on_cancel(self):
        """
        Function that called when form is canceled
        Switches app to previous form
        """
        self.parentApp.setNextFormPrevious()

    def afterEditing(self):
        """
        Lifecycle function that called after form changed
        in both submitted or canceled cases.
        """
        self.new_name.value = ""
        self.new_phone_number.value = ""
