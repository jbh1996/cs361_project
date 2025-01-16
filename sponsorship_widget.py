from PyQt6.QtWidgets import *

class Sponsorship(QWidget):

    def __init__(self,sponsorship_name, parent):
        super().__init__()
        self.parent = parent
        self.ticket_amount = 1
        self.sponsorship_name = sponsorship_name
        self._layout = QHBoxLayout()
        self._name_display = QLabel(self.sponsorship_name)
        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 100)  # Set the range of values
        self.spin_box.setValue(1)     # Set the initial value
        self._button = QPushButton("Delete", clicked= lambda: self.delete())
        self._layout.addWidget(self._name_display)
        self._layout.addWidget(self.spin_box)
        self._layout.addWidget(self.spin_box)
        self._layout.addWidget(self._button)
        self.setLayout(self._layout)
        if self.sponsorship_name == "General Attendee":
            self._button.deleteLater()
            self._layout.addWidget(QLabel("Required Field"))

    def delete(self):
        self.parent.remove_sponsorhip_level(self.sponsorship_name, self)
        self.deleteLater()
        return self._name_display

    def get_ticket_amount(self):

        return self.ticket_amount

    def get_sponsorship_name(self):

        return self.sponsorship_name