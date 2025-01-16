from PyQt6.QtWidgets import *


class Attendee(QWidget):

    def __init__(self,attendee,level_list):
        super().__init__()
        self._layout = QHBoxLayout()
        self._name_display = QLabel(attendee)
        self.dropdown_box = QComboBox()
        for level in level_list:
            self.dropdown_box.addItem(level)
        self._button = QPushButton("Delete", clicked= lambda: self.delete())
        self._layout.addWidget(self._name_display)
        self._layout.addWidget(self.dropdown_box)
        self._layout.addWidget(self._button)
        self.setLayout(self._layout)

    def add_level(self,level):
        self.dropdown_box.addItem(level)

    def remove_level(self,level):
        for num in range(self.dropdown_box.count()):
            if self.dropdown_box.itemText(num) == level:
                self.dropdown_box.removeItem(num)

    def delete(self):

        self.deleteLater()
