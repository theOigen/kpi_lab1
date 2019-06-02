from ui import ui
from api import api

if __name__ == "__main__":
    server = api.app
    server.run(debug=True)
    #UI = ui.ConsoleUI()
    #UI.run()
