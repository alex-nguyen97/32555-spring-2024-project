import sys
from cli.cli_uni_app import CLISystem
from gui.gui_uni_app import GUIUniApp
from models.database import Database

def main():
    Database()
    # Check command-line arguments to determine which interface to run
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        cli_app = CLISystem()
        cli_app.run()
    else:
        gui_app = GUIUniApp()
        gui_app.run()

if __name__ == "__main__":
    main()
