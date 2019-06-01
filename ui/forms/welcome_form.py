import npyscreen


class WelcomeForm(npyscreen.FormWithMenus):
    def all_contacts(self):
        self.parentApp.switchForm("GetCont")

    def create_contact(self):
        self.parentApp.switchForm("CreateCont")

    def exit(self):
        self.exit_editing()
        self.parentApp.setNextForm(None)

    def create(self):
        self.add(npyscreen.MultiLineEdit,
                 value="Welcome to lab1!!!\rPress ctrl+X to open menu!",
                 editable=False, relx=37, rely=7,
                 color=npyscreen.Themes.DefaultTheme.default_colors["CONTROL"])
        self.menu = self.new_menu(name="Main Menu")
        self.options = ["Get contacts", "Create contact", "Quit"]
        self.menu.addItem(self.options[0], self.all_contacts)
        self.menu.addItem(self.options[1], self.create_contact)
        self.menu.addItem(self.options[2], self.exit)
