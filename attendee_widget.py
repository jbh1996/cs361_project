from PyQt6.QtWidgets import *


class Attendee(QWidget):

    def __init__(self,attendee,level_list, parent):
        super().__init__()
        self._layout = QHBoxLayout()
        self.name = attendee
        self._name_display = QLabel(attendee)
        self.dropdown_box = QComboBox()
        self.parent = parent
        for level in level_list:
            self.dropdown_box.addItem(level)
        self._button = QPushButton("Delete", clicked= lambda: self.delete())
        self._layout.addWidget(self._name_display)
        self._layout.addWidget(self.dropdown_box)
        self._layout.addWidget(self._button)
        self.setLayout(self._layout)

    def add_level(self,level):
        self.dropdown_box.addItem(level)

    def get_attendee_name(self):

        return self.name

    def get_sponsorship_level(self):

        return self.dropdown_box.currentText()

    def remove_level(self,level):
        for num in range(self.dropdown_box.count()):
            if self.dropdown_box.itemText(num) == level:
                self.dropdown_box.removeItem(num)

    def delete(self):

        self.parent.remove_attendee(self)
        self.deleteLater()
