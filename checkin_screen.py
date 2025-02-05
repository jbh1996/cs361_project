import sys
from PyQt6.QtWidgets import *
from check_in_widget import CheckIn
from sponsorship_level_progress import SponsorshipProgress



class MainCheckInWindow(QMainWindow):
    def __init__(self, ticket_list, sponsorship_levels, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set Up Ticket List
        self.ticket_list = ticket_list
        self.widgets = []
        self.sponsorship_level_progress_widgets = []

        #Set Up Tabs
        self.tabs = QTabWidget()
        self.check_in_list_tab = QWidget()
        self.close_tab = QWidget()
        self.status_tab = QWidget()

        #Search Bar, Scroll Bar, and Check In List
        self.check_in_list_layout = QVBoxLayout()
        self._search_bar = QLineEdit(textChanged= lambda: self.filter())
        self._search_bar.setPlaceholderText("Search for Attendee Name Here")
        self.check_in_list_holder = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.check_in_list_holder_layout = QVBoxLayout()
        # Add a widget entry for each ticket
        for ticket in ticket_list:
            widget = CheckIn(ticket[0], ticket[1])
            self.widgets.append(widget)
            self.check_in_list_holder_layout.addWidget(widget)
        self.check_in_list_holder.setLayout(self.check_in_list_holder_layout)
        self.scroll.setWidget(self.check_in_list_holder)
        self.search_bar_layout = QHBoxLayout()
        self._search_label = QLabel("Search Here:")
        self.search_bar_layout.addWidget(self._search_label)
        self.search_bar_layout.addWidget(self._search_bar)
        self.check_in_list_layout.addLayout(self.search_bar_layout)
        self.filter_dropdown = QComboBox()
        self.filter_dropdown = QComboBox(currentTextChanged =  lambda: self.filter_by_sponsorship())
        self.filter_dropdown.addItem("All Sponsorship Levels")
        for level in sponsorship_levels:
            self.filter_dropdown.addItem(level)
        self.filter_layout = QHBoxLayout()
        self.filter_label = QLabel("Filter by Sponsorship Level")
        self.filter_layout.addWidget(self.filter_label)
        self.filter_layout.addWidget(self.filter_dropdown)
        self.check_in_list_layout.addLayout(self.filter_layout)
        self.attendee_labels = QHBoxLayout()
        self.attendee_label_one = QLabel("Attendee Name")
        self.attendee_label_two = QLabel("Sponsorship Level")
        self.attendee_label_three = QLabel("Checkin Status")
        self.attendee_labels.addWidget(self.attendee_label_one)
        self.attendee_labels.addWidget(self.attendee_label_two)
        self.attendee_labels.addWidget(self.attendee_label_three)
        self.check_in_list_layout.addLayout(self.attendee_labels)
        self.check_in_list_layout.addWidget(self.scroll)
        self.check_in_list_tab.setLayout(self.check_in_list_layout)
        self.tabs.addTab(self.check_in_list_tab, "Check In List")

        # Set Up Close Tab
        self.close_tab_layout = QVBoxLayout()
        self.close_tab.setLayout(self.close_tab_layout)
        self.close_button = QPushButton("Close Check in Session")
        self.close_tab_layout.addWidget(self.close_button)
        self.close_warning = QLabel("Warning! You will use all your check in statuses if you decide to close!")
        self.close_tab_layout.addWidget(self.close_warning)
        self.tabs.addTab(self.close_tab, "End Check In Session")

        # Set Up Progress by Sponsorship Level
        self.status_tab_layout = QVBoxLayout()
        self.status_tab.setLayout(self.status_tab_layout)
        self.tabs.addTab(self.status_tabb, "View Check In Status by Sponsorship Level")
        self.refresh_button = QPushButton("Refresh")
        self.progress_list_holder = QWidget()
        self.scroll_progress = QScrollArea()
        self.scroll_progress.setWidgetResizable(True)
        self.progress_holder_layout = QVBoxLayout()
        for level in sponsorship_levels:
            addition = SponsorshipProgress(level)
            self.sponsorship_level_progress_widgets.append(addition)
            self.progress_holder_layout.addWidget(addition)
        self.progress_list_holder.setLayout(self.progress_holder_layout)
        self.scroll_progress.setWidget(self.progress_list_holder)
        self.status_tab_layout.addWidget(self.refresh_button)
        self.status_tab_layout.addWidget(self.scroll_progress)

        self.setCentralWidget(self.tabs)

    def filter(self):
        for widget in self.widgets:
            if self._search_bar.text() in widget.get_attendee_name():
                widget.show()
            else:
                widget.hide()

    def filter_by_sponsorship(self):

        if self.filter_dropdown.currentText() == "All Sponsorship Levels":
            for widget in self.widgets:
                widget.show()
        else:
            for widget in self.widgets:
                if widget.get_sponsorship_level() == self.filter_dropdown.currentText():
                    widget.show()
                else:
                    widget.hide()







