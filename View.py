from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QLabel, \
    QPushButton, QGridLayout, QWidget, QSizePolicy, QMenu, QScrollArea


class CardView(QFrame):
    def __init__(self):
        """A black square"""
        super().__init__()
        self.data = None
        """The data of the card"""
        self.label = QLabel()
        """The label of the card"""
        self.layout = QVBoxLayout()
        """The layout of the card"""

    def configure(self):
        """Configure the view of the card"""
        self.setFrameStyle(QFrame.Shape.Box)
        self.setLineWidth(1)

        # Make it so it is always 1/3 of the width of the window
        # Fix it at 33% of the width
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.label.setFixedSize(260, 150)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setText(self.data)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def get_data(self):
        """Get the data from the model"""
        return self.data

    def set_data(self, data):
        """Set the data in the model"""
        self.data = data
        self.label.setText(self.data)


class ContentBoxView(QFrame):
    """The view of the content area"""

    def __init__(self):
        """Create the view of the content area"""
        super().__init__()
        self.context_menu = QMenu(self)
        """The context menu - On right click"""

        self.topbar = QWidget()
        """The topbar of the content area"""
        self.topbar_layout = QGridLayout()
        """The layout of the topbar"""
        self.topbar_label = QLabel("Choose the file type")
        """The label of the topbar"""

        self.content = QWidget()
        """The content area"""
        self.nb_cards = 0
        """The number of cards in the content area"""
        self.row = 0
        """The row of the content area"""
        self.column = 0
        """The column of the content area"""
        self.max_column = 2
        """The max column of the content area"""

        self.content_layout = QGridLayout()
        """The layout of the content area"""

        self.main_layout = QVBoxLayout()
        """The main layout of the content area"""

        self.scroll = QScrollArea()
        """The scroll area of the content area"""

        self.scroll.setMinimumWidth(300) # TODO : Move this to the presenter as it is a logic function

    def configure(self):
        """Configure the content area"""
        self.configure_topbar()
        self.configure_content()
        self.configure_content_box()
        self.configure_layouts()
        self.configure_scrollarea()

    def configure_topbar(self):
        """Configure the topbar"""
        self.topbar.setStyleSheet("background-color: #2f3136;")
        self.topbar_layout.addWidget(self.topbar_label, 0, 0)
        self.topbar_label.setStyleSheet("color: darkgrey;")
        self.topbar.setMaximumHeight(35)
        self.topbar_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def configure_layouts(self):
        """Configure the layouts of the content area"""
        self.topbar.setLayout(self.topbar_layout)
        self.content.setLayout(self.content_layout)
        self.scroll.setWidget(self.content)

        self.main_layout.addWidget(self.scroll)
        self.setLayout(self.main_layout)

    def configure_content(self):
        """Configure the content area"""
        self.content.setStyleSheet("background-color: #2f3136;")
        self.content.setSizePolicy(QSizePolicy.Policy.Expanding,
                                   QSizePolicy.Policy.Expanding)

    def configure_scrollarea(self):
        """Configure the scroll area"""
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameStyle(QFrame.Shape.NoFrame)
        self.scroll.setStyleSheet("background-color: #36393f;")
        self.scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded)

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

    def add_card(self, card : QWidget):
        """Add a card to the content area"""
        self.content_layout.addWidget(card, self.row,
                                      self.column)
        self.nb_cards += 1
        self.column += 1
        if self.column == self.max_column:
            self.column = 0
            self.row += 1

    @staticmethod
    def create_card(data):
        """Create a card"""
        card = CardView()
        card.configure()
        card.set_data(data)

    def resizeEvent(self, event):
        """Looks if a resize needs to be done"""
        card_width = 260 # TODO : Get the width of the card from the model
        possible_column = self.width() // (card_width * 1.10)
        possible_column = int(possible_column)
        if possible_column != self.max_column:
            self.max_column = possible_column
            self.update_cards()

    def update_cards(self):
        """Update the cards"""
        # Remove them all
        cards = []
        for i in reversed(range(self.content_layout.count())):
            cards.append(self.content_layout.itemAt(i).widget())
            self.content_layout.itemAt(i).widget().setParent(None)

        cards.reverse()
        self.row = 0
        self.column = 0
        for card in cards:
            self.content_layout.addWidget(card, self.row,
                                          self.column)
            self.column += 1
            if self.column == self.max_column:
                self.column = 0
                self.row += 1


class MainView:
    """Main view of the application
    It has three elements :
    - The topbar - Contains the title
    - The toolbar - Contains the buttons
    - The content area - Contains the content
    """

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
        self.content = ContentView()  # TODO: Make a content area class
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

        # Create a list containing all the buttons
        # Dictionnary containing all the buttons
        self.buttons = {
            "new"    : QPushButton("New"),
            "open"   : QPushButton("Open"),
            "save"   : QPushButton("Save"),
            "save_as": QPushButton("Save as"),
            "exit"   : QPushButton("Exit")
            }

        """The exit button"""
        self.main_layout = QGridLayout()
        """The main layout of the main window"""
        self.main_widget = QWidget()
        """The main widget of the main window"""

    def show(self):
        """Show the main window"""
        self.window.show()

    def close(self):
        """Close the main window"""
        self.window.close()

    def configure_app(self):
        """Configure the main window and all the widgets associated with it
        This includes the topbar, the toolbar and the content area and
        their layoutsmas well as the main window itself using their
        dedicated methods
        """
        # Configure the main window
        self.configure_main_window()

        # Configure three main components - topbar, toolbar, content
        self.configure_topbar()
        self.configure_toolbar()
        self.content.configure_content_box()

        # Configure the layouts
        self.configure_layouts()

        # Configure the main widget
        self.configure_main_widget()

    def configure_main_widget(self):
        """Configure the main widget of the main window (The whole view)"""
        self.main_widget.setLayout(self.main_layout)
        self.window.setCentralWidget(self.main_widget)

    def configure_topbar(self):
        """Configure the topbar"""
        self.header_widget.setFixedHeight(50)
        self.header_widget.setStyleSheet("background-color: #36393f")
        self.header_layout.addWidget(self.title)
        self.title.setStyleSheet("color: white; font-size: 20px;")

    def configure_toolbar(self):
        """Configure the toolbar"""
        self.menu_widget.setFixedWidth(100)
        self.menu_widget.setStyleSheet("background-color: #36393f")  # Dark theme

        for button in self.buttons.values():
            self.menu_layout.addWidget(button)
            button.setFixedHeight(30)
            button.setFixedWidth(60)
            button.setStyleSheet("QPushButton {background-color: #2f3136; color: white; border: 1px solid #2f3136;}"
                                 "QPushButton:hover {background-color: #40444b;}"
                                 "QPushButton:pressed {background-color: #7289da;}")
            button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.menu_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_layout.setSpacing(60)

    def configure_layouts(self):
        """Configure the layouts of the main window"""
        self.header_widget.setLayout(self.header_layout)
        self.menu_widget.setLayout(self.menu_layout)
        self.content.setLayout(self.content_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.header_widget, 0, 0, 1, 2)
        self.main_layout.addWidget(self.menu_widget, 1, 0)
        self.main_layout.addWidget(self.content, 1, 1)

    def configure_main_window(self):
        """Configure the main window"""
        self.window.setWindowTitle("Keeper 101")
        self.window.setStyleSheet("background-color: #2f3136")
        self.window.resize(800, 600)
