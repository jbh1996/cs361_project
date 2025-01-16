from PyQt6.QtWidgets import *


class Attendee(QWidget):

    def __init__(self,attendee,level_list):
        super().__init__()
        self._layout = QHBoxLayout()
        self._name_display = QLabel(attendee)
        self.dropdown_box = QComboBox()
        for level in level_list:
            self.dropdown_box.addItem(level)
        self._button = QPushButton("Delete")
        self._layout.addWidget(self._name_display)
        self._layout.addWidget(self.dropdown_box)
        self._layout.addWidget(self._button)
        self.setLayout(self._layout)

    def update_levels(self,level_list):
        self.dropdown_box.clear()
        for level in level_list:
            self.dropdown_box.addItem(level)
