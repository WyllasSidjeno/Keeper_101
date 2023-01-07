from PyQt6.QtGui import QMouseEvent

from Model import MainModel, ContentModel
from View import MainView


class ContentPresenter:
    """The presenter of the content area"""
    def __init__(self, view):
        """Create the presenter"""
        self.view = view
        """The view of the content area #Do some type hinting
        It is a QFrame"""
        self.model = ContentModel()
        """The model of the content area"""

    def run(self):
        """Run the presenter"""
        self.bind_view_click()
        self.bind_context_menu()

    def bind_view_click(self):
        """Bind the view (QFrame) to the function that will handle the click"""
        self.view.mousePressEvent = self.handle_click

    def handle_click(self, e: QMouseEvent):
        """Handle the click and call the right function"""
        if e.button().name == "RightButton":
            self.right_click(e.pos())

    def right_click(self, pos):
        """Handle the right click - Show the context menu"""
        self.view.show_context_menu(pos)

    def bind_context_menu(self):
        """Bind the context menu to the right functions"""
        print(self.view.context_menu.actions())
        self.view.context_menu.triggered.connect(self.handle_context_menu)

    def handle_context_menu(self, action):
        """Handle the context menu"""
        action_name = action.text()
        action_name = action_name.lower().replace(" ", "_")
        if action_name == "add_card":
            self.add_card()
        elif action_name == "remove":
            self.remove()
        elif action_name == "edit":
            self.edit()
        elif action_name == "add_list":
            self.add_list()

    def add_card(self):
        """Add a card"""
        print("Add a card")

    def remove(self):
        """Remove a card"""
        print("Remove a card")

    def edit(self):
        """Edit a card"""
        print("Edit a card")

    def add_list(self):
        """Move a card"""
        print("Add a list")


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
