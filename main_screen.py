import sys
from PyQt6.QtWidgets import *
from check_in_widget import CheckIn
from PyQt6.QtCore import Qt




class MainCheckInWindow(QMainWindow):
    def __init__(self, ticket_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ticket_list = ticket_list
        self.tabs = QTabWidget()
        self.check_in_list_tab = QWidget()
        self.check_in_list_layout = QVBoxLayout()
        self._search_bar = QLineEdit()
        self.check_in_list_holder = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.check_in_list_holder_layout = QVBoxLayout()
        for ticket in ticket_list:
            widget = CheckIn(ticket[0], ticket[1])
            self.check_in_list_holder_layout.addWidget(widget)
        self.check_in_list_holder.setLayout(self.check_in_list_holder_layout)
        self.scroll.setWidget(self.check_in_list_holder)
        self.check_in_list_layout.addWidget(self._search_bar)
        self.check_in_list_layout.addWidget(self.scroll)
        self.check_in_list_tab.setLayout(self.check_in_list_layout)
        self.tabs.addTab(self.check_in_list_tab, "Check In List")
        self.setCentralWidget(self.tabs)




app = QApplication(sys.argv)
w = MainCheckInWindow([("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Bill", "General Admission"),("Sarah", "Silver Level"),("Sarah", "Silver Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Bill", "General Admission"),("Sarah", "Silver Level"),("Sarah", "Silver Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Bill", "General Admission"),("Sarah", "Silver Level"),("Sarah", "Silver Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Bill", "General Admission"),("Sarah", "Silver Level"),("Sarah", "Silver Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Jacob", "Gold Level"),("Bill", "General Admission"),("Sarah", "Silver Level"),("Sarah", "Silver Level")])
w.show()
sys.exit(app.exec())
