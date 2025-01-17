import sys
from PyQt6.QtWidgets import *
from check_in_widget import CheckIn




class MainCheckInWindow(QMainWindow):
    def __init__(self, ticket_list, sponsorship_levels, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set Up Ticket List
        self.ticket_list = ticket_list

        #Set Up Tabs
        self.tabs = QTabWidget()
        self.check_in_list_tab = QWidget()
        self.close_tab = QWidget()

        #Search Bar, Scroll Bar, and Check In List
        self.check_in_list_layout = QVBoxLayout()
        self._search_bar = QLineEdit()
        self.check_in_list_holder = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.check_in_list_holder_layout = QVBoxLayout()
        # Add a widget entry for each ticket
        for ticket in ticket_list:
            widget = CheckIn(ticket[0], ticket[1])
            self.check_in_list_holder_layout.addWidget(widget)
        self.check_in_list_holder.setLayout(self.check_in_list_holder_layout)
        self.scroll.setWidget(self.check_in_list_holder)
        self.check_in_list_layout.addWidget(self._search_bar)
        self.check_in_list_layout.addWidget(self.scroll)
        self.check_in_list_tab.setLayout(self.check_in_list_layout)
        self.tabs.addTab(self.check_in_list_tab, "Check In List")

        # Set Up Close Tab
        self.close_tab_layout = QVBoxLayout()
        self.close_tab.setLayout(self.close_tab_layout)
        self.close_button = QPushButton("Close Check in Session")
        self.close_tab_layout.addWidget(self.close_button)
        self.tabs.addTab(self.close_tab, "End Check In Session")

        self.setCentralWidget(self.tabs)




