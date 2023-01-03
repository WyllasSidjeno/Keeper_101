from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QLabel, \
    QPushButton, QGridLayout, QWidget


class MainView:
    def __init__(self):
        # Using PyQt6, create an orange sidebar with a list of buttons
        # The buttons should be:
        # - New
        # - Open
        # - Save
        # - Save As
        # - Exit
        self.window = self.create_main_window()
        """ The main window of the application, which includes the 
        sidebar and the main content area
        :type: QMainWindow """

    def show(self):
        self.window.show()

    def close(self):
        print("View: close")

    def run(self):
        print("View: run")

    @staticmethod
    def create_main_window():
        # Create a frame that will contain 3 different layouts :
        # - A topbar with a title that is positionned on top of the window
        #     - It needs to be 100% width and 10% height
        # - A toolbar with the buttons (new, open, save, save as, exit)
        #     - The toolbar should be on the left side of the window
        # - A content area
        #     - The content area should be on the right side of the window, under the topbar and right of the toolbar

        # Create the main window
        window = QMainWindow()
        window.setWindowTitle("Main Window")
        window.setWindowIcon(QIcon("icon.png"))

        # Create the topbar
        header_widget = QFrame()
        header_widget.setFixedHeight(50)
        header_widget.setStyleSheet("background-color: #FFA500;") # Orange

        # Create the toolbar
        menu_widget = QFrame()
        menu_widget.setFixedWidth(100)
        menu_widget.setStyleSheet("background-color: #FFA500;") # Orange

        # Create the content area
        content = QFrame()
        content.setStyleSheet("background-color: #FFFFFF;") # White

        # Create the layouts
        header_layout = QVBoxLayout()
        menu_layout = QVBoxLayout()
        content_layout = QGridLayout()

        # Create the title
        title = QLabel("Title")
        title.setStyleSheet("font-size: 20px;")

        # Create the buttons
        new_button = QPushButton("New")
        open_button = QPushButton("Open")
        save_button = QPushButton("Save")
        save_as_button = QPushButton("Save As")
        exit_button = QPushButton("Exit")

        # Add the title to the topbar layout
        header_layout.addWidget(title)

        # Add the buttons to the toolbar layout
        menu_layout.addWidget(new_button)
        menu_layout.addWidget(open_button)
        menu_layout.addWidget(save_button)
        menu_layout.addWidget(save_as_button)
        menu_layout.addWidget(exit_button)

        # Add the layouts to the topbar, toolbar and content
        header_widget.setLayout(header_layout)
        menu_widget.setLayout(menu_layout)
        content.setLayout(content_layout)

        gridlayout = QGridLayout()

        gridlayout.addWidget(header_widget, 0, 0, 1, 2)
        gridlayout.addWidget(menu_widget, 1, 0)
        gridlayout.addWidget(content, 1, 1)

        # Set the layout of the main window
        xWidget = QWidget()
        xWidget.setLayout(gridlayout)
        window.setCentralWidget(xWidget)





        return window
