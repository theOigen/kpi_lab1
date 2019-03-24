import npyscreen
from ui_forms import \
    welcome_form as w_form, \
    all_contacts_form as ac_form, \
    create_contact_form as cc_form, \
    edit_contact_form as ec_form


class ConsoleUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", w_form.WelcomeForm, name="Main Menu")
        self.addForm("GetCont", ac_form.AllContactsForm, name="All Contacts")
        self.addForm("CreateCont", cc_form.CreateContactForm, name="Create Contact")
        self.addForm("EditCont", ec_form.EditContactForm, name="Edit Contact")

    def update_contacts_form(self):
        self.getForm("GetCont").upd()
