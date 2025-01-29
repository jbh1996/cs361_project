import sys
from PyQt6.QtWidgets import *
from sponsorship_widget import Sponsorship
from attendee_widget import Attendee
from checkin_screen import MainCheckInWindow




class EventCreationWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sponsorship_levels = ["General Attendee"]

        self.attendee_widgets = []
        self.sponsorship_widgets = []

        #Set Up Tabs
        self.tabs = QTabWidget()
        self.showMaximized()
        self.sponsorship_list_tab = QWidget()
        self.attendee_list_tab = QWidget()
        self.launch_tab = QWidget()

        #Set Up Sponsorship List Tab Widgets and Layouts
        self.sponsorship_tab_layout = QVBoxLayout()
        self.sponsorship_list_tab.setLayout(self.sponsorship_tab_layout)
        self.input_bar = QLineEdit(returnPressed= lambda: self.add_sponsorship_level())
        self.input_bar.setPlaceholderText("Enter Your Sponsorship Level Name Here")
        self.add_button = QPushButton("Add Level", clicked= lambda: self.add_sponsorship_level())
        self.sponsorship_list_holder = QWidget()
        self.scroll_sponsorship = QScrollArea()
        self.sponsorship_list_holder_layout = QVBoxLayout()

        #Add Input Bar and Push button
        self.sponsorship_addition_layout = QHBoxLayout()
        self.sponsorship_addition_layout.addWidget(self.input_bar)
        self.sponsorship_addition_layout.addWidget(self.add_button)
        self.sponsorship_tab_layout.addLayout(self.sponsorship_addition_layout)

        # Set Up Labels
        self.sponsorship_labels = QHBoxLayout()
        self.sponsorship_label_one = QLabel("Sponsorship Level")
        self.sponsorship_label_two = QLabel("Tickets per Level")
        self.sponsorship_label_three = QLabel("Delete: Warning! This will affect all attendee dropdowns.")
        self.sponsorship_labels.addWidget(self.sponsorship_label_one)
        self.sponsorship_labels.addWidget(self.sponsorship_label_two)
        self.sponsorship_labels.addWidget(self.sponsorship_label_three)
        self.sponsorship_tab_layout.addLayout(self.sponsorship_labels)




        #set scroll to sponsorship levels
        self.scroll_sponsorship.setWidget(self.sponsorship_list_holder)
        self.sponsorship_tab_layout.addWidget(self.scroll_sponsorship)
        self.scroll_sponsorship.setWidgetResizable(True)

        #Add Sponsorship Levels from List
        for level in self.sponsorship_levels:
            widget = Sponsorship(level, self)
            self.sponsorship_widgets.append(widget)
            self.sponsorship_list_holder_layout.addWidget(widget)

        self.sponsorship_list_holder.setLayout(self.sponsorship_list_holder_layout)
        self.tabs.addTab(self.sponsorship_list_tab, "Step 1: Create Sponsorship List")

        #Set Up Attendee Tab
        self.attendee_tab_layout = QVBoxLayout()
        self.attendee_list_tab.setLayout(self.attendee_tab_layout)
        self.attendee_input = QLineEdit(returnPressed= lambda: self.add_attendee())
        self.attendee_input.setPlaceholderText("Enter Your Attendee Name Here")
        self.attendee_button = QPushButton("Add Attendee", clicked= lambda: self.add_attendee())
        self.attendee_list_holder = QWidget()
        self.scroll_attendee = QScrollArea()
        self.attendee_holder_layout = QVBoxLayout()

        self.attendee_addition_layout = QHBoxLayout()
        self.attendee_addition_layout.addWidget(self.attendee_input)
        self.attendee_addition_layout.addWidget(self.attendee_button)
        self.attendee_tab_layout.addLayout(self.attendee_addition_layout)

        # Set Up Labels
        self.attendee_labels = QHBoxLayout()
        self.attendee_label_one = QLabel("Attendee Name")
        self.attendee_label_two = QLabel("Sponsorship Level")
        self.attendee_label_three = QLabel("Delete?")
        self.attendee_labels.addWidget(self.attendee_label_one)
        self.attendee_labels.addWidget(self.attendee_label_two)
        self.attendee_labels.addWidget(self.attendee_label_three)
        self.attendee_tab_layout.addLayout(self.attendee_labels)

        self.scroll_attendee.setWidget(self.attendee_list_holder)
        self.attendee_tab_layout.addWidget(self.scroll_attendee)
        self.scroll_attendee.setWidgetResizable(True)


        self.attendee_list_holder.setLayout(self.attendee_holder_layout)
        self.tabs.addTab(self.attendee_list_tab, "Step 2: Add Attendees")



        # Set Up Launch Tab
        self.launch_tab_layout = QVBoxLayout()
        self.launch_tab.setLayout(self.launch_tab_layout)
        self.launch_button = QPushButton("Launch Check in Session", clicked= lambda: self.launch_checkin_window())
        self.launch_tab_layout.addWidget(self.launch_button)
        self.tabs.addTab(self.launch_tab, "Step 3: Launch Check in Session")
        self.setCentralWidget(self.tabs)

    def add_attendee(self):
        if self.attendee_input.text() == "":
            return
        else:
            widget = Attendee(self.attendee_input.text(), self.sponsorship_levels, self)
            self.attendee_widgets.append(widget)
            self.attendee_holder_layout.addWidget(widget)

    def add_sponsorship_level(self):
        if self.input_bar.text() == "":
            return
        elif self.input_bar.text() in self.sponsorship_levels:
            return
        else:
            widget = Sponsorship(self.input_bar.text(), self)
            self.sponsorship_widgets.append(widget)
            self.sponsorship_list_holder_layout.addWidget(widget)
            self.sponsorship_levels.append(self.input_bar.text())
            self.add_attendee_level(self.input_bar.text())

    def remove_sponsorship_level(self, level, widget):

        self.sponsorship_levels.remove(level)
        self.sponsorship_widgets.remove(widget)
        for attendee_widget in self.attendee_widgets:
            attendee_widget.remove_level(level)

    def remove_attendee(self, widget):

        self.attendee_widgets.remove(widget)

    def add_attendee_level(self,level):

        for attendee_widget in self.attendee_widgets:
            attendee_widget.add_level(level)

    def launch_checkin_window(self):

        ticket_dictionary = {}
        ticket_array = []
        for widget in self.sponsorship_widgets:
            ticket_dictionary[widget.get_sponsorship_name()] = widget.get_spin_box_value()

        for widget in self.attendee_widgets:
            for num in range(ticket_dictionary[widget.get_sponsorship_level()]):
                ticket_array.append((widget.get_attendee_name(), widget.get_sponsorship_level()))

        self.window = MainCheckInWindow(ticket_array, self.sponsorship_levels)
        self.window.showMaximized()

app = QApplication(sys.argv)
w = EventCreationWindow()
w.show()
sys.exit(app.exec())