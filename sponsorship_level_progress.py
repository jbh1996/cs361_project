

from PyQt6.QtWidgets import *
import time


class SponsorshipProgress(QWidget):

    def __init__(self, sponsorship_level):
        super().__init__()
        self._sponsorship_level = sponsorship_level
        self._progress = 0
        self._layout = QHBoxLayout()
        self._name_display = QLabel(self._sponsorship_level)
        self._progress_display = QLabel(str(self._progress))
        self._layout.addWidget(self._name_display)
        self._layout.addWidget(self._progress_display)
        self.setLayout(self._layout)

    def update_progress(self, updated_number):
        """Update Progress"""
        self._progress = updated_number

    def get_sponsorship_level(self):

        return self._sponsorship_level

