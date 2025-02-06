import json
import sys
from PyQt6.QtWidgets import *
from check_in_widget import CheckIn
from sponsorship_level_progress import SponsorshipProgress
from Attendee_Monitior_Widget import AttendeeMonitor
import zmq
import datetime
import csv

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
        self.time_tab = QWidget()
        self.csv_tab = QWidget()
        self.monitor_tab = QWidget()


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


        # Set Up Monitor Tab
        self.monitor_layout = QVBoxLayout()
        self.monitor_tab.setLayout(self.monitor_layout)
        self.tabs.addTab(self.status_tab, "View Latest Checkins")
        self.monitor_strip_layout = QHBoxLayout()
        self.monitor_spin_box_label = QLabel("See attendees checked in for the past X minutes:")
        self.monitor_spin_box = QSpinBox()
        self.monitor_spin_box.setRange(1, 300)
        self.monitor_spin_box.setValue(1)
        self.monitor_button = QPushButton("Refresh", clicked= lambda: self.get_latest_checkins())
        self.monitor_strip_layout.addWidget(self.monitor_spin_box_label)
        self.monitor_strip_layout.addWidget(self.monitor_spin_box)
        self.monitor_strip_layout.addWidget(self.monitor_button)
        self.monitor_list_holder = QWidget()
        self.scroll_monitor = QScrollArea()
        self.scroll_monitor.setWidgetResizable(True)
        self.monitor_holder_layout = QVBoxLayout()
        self.monitor_list_holder.setLayout(self.monitor_holder_layout)
        self.scroll_monitor.setWidget(self.monitor_list_holder)
        self.monitor_labels = QHBoxLayout()
        self.monitor_labels.addWidget(QLabel("Attendee Name"))
        self.monitor_labels.addWidget(QLabel("Sponsorship Level"))
        self.monitor_layout.addLayout(self.monitor_strip_layout)
        self.monitor_layout.addLayout(self.monitor_labels)
        self.monitor_layout.addWidget(self.scroll_monitor)

        # Set Up Progress by Sponsorship Level
        self.status_tab_layout = QVBoxLayout()
        self.status_tab.setLayout(self.status_tab_layout)
        self.tabs.addTab(self.status_tab, "View Check In Status by Sponsorship Level")
        self.refresh_button = QPushButton("Refresh", clicked= lambda: self.get_progress())
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
        self.progress_labels = QHBoxLayout()
        self.progress_labels.addWidget(QLabel("Sponsorship Level"))
        self.progress_labels.addWidget(QLabel("Percentage Checked In"))
        self.status_tab_layout.addLayout(self.progress_labels)
        self.status_tab_layout.addWidget(self.scroll_progress)

        # Set Up Time Tab
        self.time_tab_layout = QVBoxLayout()
        self.time_tab.setLayout(self.time_tab_layout)
        self.time_settings_layout = QHBoxLayout()
        self.time_settings_label = QLabel("Minutes for Open Check-In:")
        self.time_spin_box = QSpinBox()
        self.time_spin_box.setRange(15, 300)
        self.time_spin_box.setValue(15)
        self.time_refresh_button = QPushButton("Refresh Time Window", clicked = lambda: self.time_refresh())
        self.time_settings_layout.addWidget(self.time_settings_label)
        self.time_settings_layout.addWidget(self.time_spin_box)
        self.time_settings_layout.addWidget(self.time_refresh_button)
        self.time_remaining_layout = QHBoxLayout()
        self.time_remaining_label = QLabel("Time Remaining: ")
        self.time_remaining_clock = QLabel("Click Refresh to See Remaining Time")
        self.time_remaining_layout.addWidget(self.time_remaining_label)
        self.time_remaining_layout.addWidget(self.time_remaining_clock)
        self.time_elapsed_layout = QHBoxLayout()
        self.time_elapsed_label = QLabel("Time Elapsed: ")
        self.time_elapsed_clock = QLabel("Click Refresh to See Elapsed Time")
        self.time_elapsed_layout.addWidget(self.time_elapsed_label)
        self.time_elapsed_layout.addWidget(self.time_elapsed_clock)
        self.time_tab_layout.addLayout(self.time_settings_layout)
        self.time_tab_layout.addLayout(self.time_remaining_layout)
        self.time_tab_layout.addLayout(self.time_elapsed_layout)
        self.tabs.addTab(self.time_tab, "Time Information")

        # Set Up CSV Tab
        self.csv_tab_layout = QVBoxLayout()
        self.csv_tab.setLayout(self.csv_tab_layout)
        self.csv_button = QPushButton("Generate CSV", clicked= lambda: self.generate_csv())
        self.csv_tab_layout.addWidget(self.csv_button)
        self.tabs.addTab(self.csv_tab, "Export CSV")

        self.setCentralWidget(self.tabs)


    def time_refresh(self):
        pass

    def generate_csv(self):
        send_array = []
        for widget in self.widgets:
            append_array = []
            append_array.append(widget.get_attendee_name())
            append_array.append(widget.get_sponsorship_level())
            append_array.append(widget.get_check_in_status())
            append_array.append(widget.get_check_in_time())
            send_array.append(append_array)
        message_string = json.dumps(send_array)
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5556")
        socket.send_string(message_string)
        csv_string = socket.recv_string()
        with open(f"{datetime.datetime.now()}CheckInStatus.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            rows = csv_string.split("\n")
            for row in rows:
                fields = row.split(",")
                writer.writerow(fields)

    def filter(self):
        for widget in self.widgets:
            if self._search_bar.text() in widget.get_attendee_name():
                widget.show()
            else:
                widget.hide()

    def get_latest_checkins(self):
        pass

    def get_progress(self):
        message_string = ""
        for widget in self.widgets:
            append_string = widget.get_sponsorship_level()+ ";" + str(widget.get_check_in_status()) + ","
            message_string += append_string

        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        socket.send_string(message_string)
        json_string = socket.recv_string()
        response_dict = json.loads(json_string)
        for widget in self.sponsorship_level_progress_widgets:
            if widget.get_sponsorship_level() in response_dict:
                widget.update_progress(response_dict[widget.get_sponsorship_level()])

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







