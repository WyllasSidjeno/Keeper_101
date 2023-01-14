"""Represents the Controller in the MVC pattern of the application."""
from PyQt6.QtGui import QMouseEvent
from Model import MainModel, ContentModel
from View import MainView
from View import create_card


class ContentController:
    """The controller of the content area"""

    def __init__(self, view):
        """Create the controller"""
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

    def bind_context_menu(self):
        """Bind the context menu to the right functions"""
        self.view.context_menu.triggered.connect(self.handle_context_menu)

    def handle_click(self, e: QMouseEvent):
        """Handle the click and call the right function"""
        if e.button().name == "RightButton":
            self.view.show_context_menu(e.pos())

    def handle_context_menu(self, chosen_option):
        """Handle the context menu"""
        chosen_option = chosen_option.text().lower().replace(" ", "_")
        getattr(self, chosen_option)()

    def add_card(self):
        """Add a card"""
        card = create_card()
        self.view.add_card(card)

    def remove(self):
        """Remove a card"""
        # Get the user mouse posisition
        mouse_pos = self.view.mapFromGlobal(self.view.cursor().pos())
        # Get the position of all the cards
        print(mouse_pos)
        self.view.content.get_card_position()

    def edit(self):
        """Edit a card"""
        print("Edit a card")

    def add_list(self):
        """Move a card"""
        print("Add a list")


class MainController:
    """This is the main function of the application.
    It is the one that will
    create the main window and the main controller. It is the one that will
    start the application. It is the one that will handle the events. It is
    the one that will handle the logic of the application.
    """

    def __init__(self):
        """Create the main controller
        It is the main class of the application. It is the one that will
        communicate with the model and the view. It is the one that will
        handle the events. It is the one that will handle the logic of the
        application."""
        self.view = MainView()
        """The view of the main window"""
        self.model = MainModel()
        """The model of the main window"""
        self.ContentPresenter = ContentController(self.view.content)
        """The presenter of the content area"""

    def run(self):
        """Start the application
        This function will start the application. It will create the main
        window and the main presenter."""
        self.view.configure_app()
        self.view.show()
        self.bind_all_buttons()
        self.ContentPresenter.run()

    def get_data(self):
        """Get the data from the model"""
        # TODO : Get a specific data instead of all the data
        return self.model.get_data()

    def set_data(self, data):
        # TODO : Set a specific data instead of all the data
        """Set the data in the model"""
        self.model.set_data(data)

    def close(self):
        """Close the application"""
        self.view.close()

    def on_new_clicked(self):
        """Open a menu to create a new file"""
        print("New clicked")

    def on_open_clicked(self):
        """Open a menu to open a file"""
        print("Open clicked")

    def on_save_clicked(self):
        """Save the data"""
        print("Save clicked")

    def on_save_as_clicked(self):
        """Save the data as a new file"""
        print("Save as clicked")

    def on_exit_clicked(self):
        """Exit the application, pretty much a wrapper for close"""
        print("Exit clicked")
        self.close()

    def bind_all_buttons(self):
        """Bind all the buttons to their respective functions"""
        for button in self.view.buttons:
            method = getattr(self, "on_" + button + "_clicked")
            bind_widget(self.view.buttons[button], method)


def bind_widget(widget, method):
    """Bind a widget to a method"""
    from PyQt6.QtWidgets import QAbstractButton
    if isinstance(widget, QAbstractButton):
        # noinspection PyUnresolvedReferences
        widget.clicked.connect(method)
