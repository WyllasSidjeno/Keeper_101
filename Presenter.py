from PyQt6.QtGui import QMouseEvent

from Model import MainModel, ContentModel
from View import MainView


class MainPresenter:
    def __init__(self):
        self.view = MainView()
        self.model = MainModel()

    def bind_all_buttons(self):
        # TODO : Test this function
       for button in self.view.buttons:
           button.clicked.connect(self.button_clicked)

    def get_data(self):
        return self.model.get_data()

    def set_data(self, data):
        self.model.set_data(data)

    def show(self):
        self.view.show()

    def close(self):
        self.view.close()

def bind_widget(widget, method, signal):
    # Todo : Implement a for each loop to bind all the widgets sent
    widget.connect(method, signal)
