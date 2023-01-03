from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QLabel, \
    QPushButton, QGridLayout, QWidget


class MainView:
    def __init__(self):
        """Create the main window and all the widgets associated with it

        It has three elements :
        - The topbar - Contains the title
        - The toolbar - Contains the buttons
        - The content area - Contains the content
        """
        # Starts by creating the main window
        self.window = QMainWindow()
        """The main window"""

        # Creates the main widgets
        self.header_widget = QFrame()
        """The topbar"""
        self.menu_widget = QFrame()
        """The toolbar"""
        self.content = QFrame()
        """The content area"""

        # Creates the layouts for the widgets
        self.header_layout = QVBoxLayout()
        """The layout of the topbar"""
        self.menu_layout = QVBoxLayout()
        """The layout of the toolbar"""
        self.content_layout = QGridLayout()
        """The layout of the content area"""

        # Creates the topbar widgets
        self.title = QLabel("Keeper 101")
        """The title"""

        # Creates the toolbar widgets
        self.new_button = QPushButton("New")
        """The new button"""
        self.open_button = QPushButton("Open")
        """The open button"""
        self.save_button = QPushButton("Save")
        """The save button"""
        self.save_as_button = QPushButton("Save as")
        """The save as button"""
        self.exit_button = QPushButton("Exit")
        """The exit button"""

        self.main_layout = QGridLayout()
        """The main layout of the main window"""
        self.main_widget = QWidget()
        """The main widget of the main window"""

        self.configure_app()
        """ Configures the main window and all the widgets associated with it"""

    def show(self):
        self.window.show()

    def close(self):
        self.window.close()

    def configure_app(self):
        # Change the window title name
        self.window.setWindowTitle("Keeper 101")

    def configure_main_widget(self):
        self.main_widget.setLayout(self.main_layout)
        self.window.setCentralWidget(self.main_widget)




    def configure_topbar(self):
        self.header_widget.setFixedHeight(50)
        self.header_widget.setStyleSheet("background-color: #36393f")
        self.header_layout.addWidget(self.title)
        self.title.setStyleSheet("font-size: 20px;")

    def configure_toolbar(self):
        self.menu_widget.setFixedWidth(100)
        self.menu_widget.setStyleSheet("background-color: #36393f")

        self.menu_layout.addWidget(self.new_button)
        self.menu_layout.addWidget(self.open_button)
        self.menu_layout.addWidget(self.save_button)
        self.menu_layout.addWidget(self.save_as_button)
        self.menu_layout.addWidget(self.exit_button)

    def configure_content(self):
        self.content.setStyleSheet("background-color: #FFFFFF;")

    def configure_layouts(self):
        self.header_widget.setLayout(self.header_layout)
        self.menu_widget.setLayout(self.menu_layout)
        self.content.setLayout(self.content_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.header_widget, 0, 0, 1, 2)
        self.main_layout.addWidget(self.menu_widget, 1, 0)
        self.main_layout.addWidget(self.content, 1, 1)



