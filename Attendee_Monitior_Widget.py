from PyQt6.QtWidgets import *
import time


class AttendeeMonitor(QWidget):

    def __init__(self, sponsorship_level, attendee_name):
        super().__init__()
        self._sponsorship_level = sponsorship_level
        self._attendee_name = attendee_name
        self._layout = QHBoxLayout()
        self._name_display = QLabel(self._sponsorship_level)
        self._attendee_name= QLabel(attendee_name)
        self._layout.addWidget(self._attendee_name)
        self._layout.addWidget(self._name_display)
        self.setLayout(self._layout)


