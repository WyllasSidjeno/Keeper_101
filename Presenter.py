from Model import MainModel
from View import MainView


class MainPresenter:
    def __init__(self):
        self.view = MainView()
        self.model = MainModel()

    def get_data(self):
        return self.model.get_data()

    def set_data(self, data):
        self.model.set_data(data)

    def show(self):
        self.view.show()

    def close(self):
        self.view.close()