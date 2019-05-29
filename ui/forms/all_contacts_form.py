import npyscreen


class AllContactsForm(npyscreen.ActionFormV2):
    def upd(self):
        self.choosen_contact.values = [ob.to_dict() for ob in self.parentApp.contacts_manager.get_contacts()]
        self.choosen_contact.value = None
        self.my_choice.value = None

    def create(self):
        self.choosen_contact = self.add(npyscreen.TitleSelectOne, max_height=4, name="Choose any contact",
                                        values=[ob.to_dict() for ob in self.parentApp.contacts_manager.get_contacts()],
                                        value=None, scroll_exit=True)
        self.menu = ["Edit contact", "Delete contact"]
        self.my_choice = self.add(npyscreen.TitleSelectOne, max_height=3, name="What you want to do with contact?",
                                  values=self.menu, scroll_exit=True)

    def on_ok(self):
        if len(self.my_choice.value) < 1 or len(self.choosen_contact.value) < 1:
            npyscreen.notify_wait("Please, to submit the form you must choose the contact and the action!",
                                  title="Error occurred")
        elif self.my_choice.get_selected_objects()[0] == self.menu[0]:
            self.parentApp.getForm("EditCont").set_contact(self.parentApp.contacts_manager
                                                           .get_contact_by_index(self.choosen_contact.value[0]))
            self.parentApp.switchForm("EditCont")
        elif self.my_choice.get_selected_objects()[0] == self.menu[1]:
            answer = npyscreen.notify_yes_no("Are you sure?", title="Delete Contact", editw=1)
            if answer:
                self.parentApp.contacts_manager.delete_contact(self.choosen_contact.value[0])
                self.upd()

    def on_cancel(self):
        self.parentApp.setNextFormPrevious()
