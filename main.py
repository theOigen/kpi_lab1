from ui import ui
from api import api

if __name__ == "__main__":
    UI = ui.ConsoleUI()
    #UI.run()
    server = api.app
    server.run(debug=True)
