"""This represents the engine of the application."""
import sys
from PyQt6.QtWidgets import QApplication
from Controller import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    presentation = MainController()
    presentation.run()
    sys.exit(app.exec())
