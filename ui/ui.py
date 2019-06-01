import npyscreen
from src.contacts import ContactsManager
from ui.forms import \
    create_contact_form as cc_form, \
    welcome_form as w_form, \
    all_contacts_form as ac_form, \
    edit_contact_form as ec_form


class ConsoleUI(npyscreen.NPSAppManaged):
    def __init__(self):
        super().__init__()
        self.contacts_manager = ContactsManager()

    def onStart(self):
        self.contacts_manager.load_contacts()
        self.addForm("MAIN", w_form.WelcomeForm, name="Main Menu")
        self.addForm("GetCont", ac_form.AllContactsForm, name="All Contacts")
        self.addForm("CreateCont", cc_form.CreateContactForm,
                     name="Create Contact")
        self.addForm("EditCont", ec_form.EditContactForm, name="Edit Contact")

    def update_contacts_form(self):
        self.getForm("GetCont").upd()

    def onCleanExit(self):
        self.contacts_manager.save_contacts()
