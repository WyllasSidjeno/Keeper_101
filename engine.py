"""This represents the engine of the application."""
import sys
from PyQt6.QtWidgets import QApplication
from Presenter import MainPresenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    presentation = MainPresenter()
    presentation.run()
    sys.exit(app.exec())
