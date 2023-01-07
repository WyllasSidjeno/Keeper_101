from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QLabel, \
    QPushButton, QGridLayout, QWidget, QSizePolicy, QMenu


class ContentView(QFrame):
    """The view of the content area"""
    def __init__(self):
        """Create the view of the content area"""
        super().__init__()
        self.context_menu = QMenu(self)

    def configure_content_box(self):
        """Configure the content area"""
        self.setStyleSheet("background-color: #36393f;")  # Dark theme
        self.create_context_menu()
        self.context_menu.setStyleSheet("background-color: #36393f;")
        self.customContextMenuRequested.connect(self.show_context_menu)

    def create_context_menu(self):
        """Create the context menu"""
        self.context_menu.addAction("Add Card")
        self.context_menu.addAction("Remove")
        self.context_menu.addAction("Edit")
        self.context_menu.addAction("Add List")
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)


    def show_context_menu(self, point: QPoint):
        """Show the context menu"""
        self.context_menu.exec(self.mapToGlobal(point))


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

        # Change for a self.button.type = QPushButton("TypeText")
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

        # Configures the app. This includes the main app window and its three
        # components.
        self.configure_app()

    def show(self):
        self.window.show()

    def close(self):
        self.window.close()

    def configure_app(self):
        # Configure the main window
        self.configure_main_window()

        # Configure three main components - topbar, toolbar, content
        self.configure_topbar()
        self.configure_toolbar()
        self.configure_content()

        # Configure the layouts
        self.configure_layouts()

        # Configure the main widget
        self.configure_main_widget()

    def configure_main_widget(self):
        self.main_widget.setLayout(self.main_layout)
        self.window.setCentralWidget(self.main_widget)

    def configure_topbar(self):
        self.header_widget.setFixedHeight(50)
        self.header_widget.setStyleSheet("background-color: #36393f")
        self.header_layout.addWidget(self.title)
        self.title.setStyleSheet("color: white; font-size: 20px;")

    def configure_toolbar(self):
        self.menu_widget.setFixedWidth(100)
        self.menu_widget.setStyleSheet("background-color: #36393f")  # Dark theme

        self.menu_layout.addWidget(self.new_button)
        self.menu_layout.addWidget(self.open_button)
        self.menu_layout.addWidget(self.save_button)
        self.menu_layout.addWidget(self.save_as_button)
        self.menu_layout.addWidget(self.exit_button)

        for button in [self.new_button, self.open_button, self.save_button,
                       self.save_as_button, self.exit_button]:
            button.setFixedHeight(30)
            button.setFixedWidth(60)
            # Give it a dynamic animation when the mouse hovers over it and when it clicks on it.
            button.setStyleSheet("QPushButton {background-color: #2f3136; color: white; border: 1px solid #2f3136;}"
                                 "QPushButton:hover {background-color: #40444b;}"
                                 "QPushButton:pressed {background-color: #7289da;}")
            button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.menu_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_layout.setSpacing(60)

    def configure_content(self):
        self.content.setStyleSheet("background-color: #36393f;")  # Dark theme

    def configure_layouts(self):
        self.header_widget.setLayout(self.header_layout)
        self.menu_widget.setLayout(self.menu_layout)
        self.content.setLayout(self.content_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.header_widget, 0, 0, 1, 2)
        self.main_layout.addWidget(self.menu_widget, 1, 0)
        self.main_layout.addWidget(self.content, 1, 1)

    def configure_main_window(self):
        self.window.setWindowTitle("Keeper 101")
        self.window.setStyleSheet("background-color: #2f3136")
        self.window.resize(800, 600)
