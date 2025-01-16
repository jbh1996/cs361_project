from PyQt6.QtWidgets import *

class Sponsorship(QWidget):

    def __init__(self,sponsorship_name):
        super().__init__()
        self.ticket_amount = 1
        self._layout = QHBoxLayout()
        self._name_display = QLabel(sponsorship_name)
        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 100)  # Set the range of values
        self.spin_box.setValue(1)     # Set the initial value
        self._button = QPushButton("Delete", clicked= lambda: self.delete())
        self._layout.addWidget(self._name_display)
        self._layout.addWidget(self.spin_box)
        self._layout.addWidget(self.spin_box)
        self._layout.addWidget(self._button)
        self.setLayout(self._layout)

    def delete(self):

        self.deleteLater()
        return self._name_display
