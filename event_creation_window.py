import sys
from PyQt6.QtWidgets import *
from sponsorship_widget import Sponsorship
from PyQt6.QtCore import Qt




class EventCreationWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sponsorship_levels = ["General Attendee"]

        #Set Up Tabs
        self.tabs = QTabWidget()
        self.sponsorship_list_tab = QWidget()
        self.attendee_list_tab = QWidget()
        self.launch_tab = QWidget()

        #Set Up Sponsorship List Tab
        self.sponsorship_tab_layout = QVBoxLayout()
        self.sponsorship_list_tab.setLayout(self.sponsorship_tab_layout)
        self.input_bar = QLineEdit()
        self.add_button = QPushButton("Add Level")
        self.sponsorship_tab_layout.addWidget(self.input_bar)
        self.sponsorship_tab_layout.addWidget(self.add_button)
        self.sponsorship_list_holder = QWidget()
        self.sponsorship_list_holder_layout = QVBoxLayout()
        self.scroll_sponsorship = QScrollArea()
        self.scroll_sponsorship.setWidget(self.sponsorship_list_holder)
        self.sponsorship_tab_layout.addWidget(self.scroll_sponsorship)
        self.scroll_sponsorship.setWidgetResizable(True)
        for level in self.sponsorship_levels:
            widget = Sponsorship(level)
            self.sponsorship_list_holder_layout.addWidget(widget)
        self.sponsorship_list_holder.setLayout(self.sponsorship_list_holder_layout)
        self.sponsorship_tab_layout.addWidget(self.sponsorship_list_holder)
        self.tabs.addTab(self.sponsorship_list_tab, "Sponsorship List")




        # Set Up Launch Tab
        self.launch_tab_layout = QVBoxLayout()
        self.launch_tab.setLayout(self.launch_tab_layout)
        self.launch_button = QPushButton("Launch Check in Session")
        self.launch_tab_layout.addWidget(self.launch_button)
        self.tabs.addTab(self.launch_tab, "Launch Check in Session")

        self.setCentralWidget(self.tabs)
"""
        #Search Bar, Scroll Bar, and Check In List
        self.check_in_list_layout = QVBoxLayout()
        self._search_bar = QLineEdit()
        self.check_in_list_holder = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.check_in_list_holder_layout = QVBoxLayout()
        # Add a widget entry for each ticket
        self.check_in_list_holder.setLayout(self.check_in_list_holder_layout)
        self.scroll.setWidget(self.check_in_list_holder)
        self.check_in_list_layout.addWidget(self._search_bar)
        self.check_in_list_layout.addWidget(self.scroll)
        self.check_in_list_tab.setLayout(self.check_in_list_layout)
        self.tabs.addTab(self.check_in_list_tab, "Check In List")
"""




app = QApplication(sys.argv)
w = EventCreationWindow()
w.show()
sys.exit(app.exec())