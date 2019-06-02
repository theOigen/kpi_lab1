import npyscreen


class WelcomeForm(npyscreen.FormWithMenus):
    def all_contacts(self):
        """
        Function that switches app to AllContacts form
        """
        self.parentApp.switchForm("GetCont")

    def create_contact(self):
        """
        Function that switches app to CreateContact form
        """
        self.parentApp.switchForm("CreateCont")

    def exit(self):
        """
        Function that called when the user exits the main form.
        Stops the application
        """
        self.exit_editing()
        self.parentApp.setNextForm(None)

    def create(self):
        """
        Lifecycle function that called when form already initialized.
        Setup the form
        """
        self.add(npyscreen.MultiLineEdit,
                 value="Welcome to lab1!!!\rPress ctrl+X to open menu!",
                 editable=False, relx=37, rely=7,
                 color=npyscreen.Themes.DefaultTheme.default_colors["CONTROL"])
        self.menu = self.new_menu(name="Main Menu")
        self.options = ["Get contacts", "Create contact", "Quit"]
        self.menu.addItem(self.options[0], self.all_contacts)
        self.menu.addItem(self.options[1], self.create_contact)
        self.menu.addItem(self.options[2], self.exit)
