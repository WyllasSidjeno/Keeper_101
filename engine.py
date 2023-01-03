import sys
from PyQt6.QtWidgets import QApplication
from Presenter import MainPresenter

if __name__ == '__main__':
    # Create the main presentation and a app using pyqt6
    app = QApplication(sys.argv)
    presentation = MainPresenter()
    presentation.show()
    sys.exit(app.exec())
