import sys
from PyQt6.QtWidgets import *
from sponsorship_widget import Sponsorship
from attendee_widget import Attendee
from PyQt6.QtCore import Qt




class EventCreationWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sponsorship_levels = ["General Attendee"]
        self.attendees = ["Jacob"]

        #Set Up Tabs
        self.tabs = QTabWidget()
        self.sponsorship_list_tab = QWidget()
        self.attendee_list_tab = QWidget()
        self.launch_tab = QWidget()

        #Set Up Sponsorship List Tab Widgets and Layouts
        self.sponsorship_tab_layout = QVBoxLayout()
        self.sponsorship_list_tab.setLayout(self.sponsorship_tab_layout)
        self.input_bar = QLineEdit()
        self.add_button = QPushButton("Add Level")
        self.sponsorship_list_holder = QWidget()
        self.scroll_sponsorship = QScrollArea()
        self.sponsorship_list_holder_layout = QVBoxLayout()

        #Add Input Bar and Push button
        self.sponsorship_tab_layout.addWidget(self.input_bar)
        self.sponsorship_tab_layout.addWidget(self.add_button)

        #set scroll to sponsorship levels
        self.scroll_sponsorship.setWidget(self.sponsorship_list_holder)
        self.sponsorship_tab_layout.addWidget(self.scroll_sponsorship)
        self.scroll_sponsorship.setWidgetResizable(True)

        #Add Sponsorship Levels from List
        for level in self.sponsorship_levels:
            widget = Sponsorship(level)
            self.sponsorship_list_holder_layout.addWidget(widget)

        self.sponsorship_list_holder.setLayout(self.sponsorship_list_holder_layout)
        self.tabs.addTab(self.sponsorship_list_tab, "Sponsorship List")

        #Set Up Attendee Tab
        self.attendee_tab_layout = QVBoxLayout()
        self.attendee_list_tab.setLayout(self.attendee_tab_layout)
        self.attendee_input = QLineEdit()
        self.attendee_button = QPushButton("Add Attendee")
        self.attendee_tab_layout.addWidget(self.attendee_input)
        self.attendee_tab_layout.addWidget(self.attendee_button)
        self.attendee_holder_layout = QVBoxLayout()
        self.scroll_attendee = QScrollArea()
        self.attendee_list_holder = QWidget()
        self.scroll_attendee.setWidget(self.attendee_list_holder)
        for attendee in self.attendees:
            widget = Attendee(attendee, self.sponsorship_levels)
            self.attendee_holder_layout.addWidget(widget)
        self.attendee_list_holder.setLayout(self.attendee_holder_layout)

        self.attendee_tab_layout.addWidget(self.scroll_attendee)
        self.tabs.addTab(self.attendee_list_tab, "Attendee Tab")



        # Set Up Launch Tab
        self.launch_tab_layout = QVBoxLayout()
        self.launch_tab.setLayout(self.launch_tab_layout)
        self.launch_button = QPushButton("Launch Check in Session")
        self.launch_tab_layout.addWidget(self.launch_button)
        self.tabs.addTab(self.launch_tab, "Launch Check in Session")

        self.setCentralWidget(self.tabs)




app = QApplication(sys.argv)
w = EventCreationWindow()
w.show()
sys.exit(app.exec())