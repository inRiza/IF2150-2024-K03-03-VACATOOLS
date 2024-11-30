# navbar.py
from PyQt5.QtWidgets import QToolBar, QPushButton, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class Navbar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)

        self.setMovable(False)  # Lock the Navbar
        self.setStyleSheet("""
            QToolBar {
                background-color: #1c0d52;
                height: 200px;
            }
            QPushButton {
                color: white;
                background-color: transparent;
                border: none;
                font-size: 14px;
                padding: 25px 16px;
                border-radius: 5px;
                text-align: center;
                vertical-align: middle;
            }
            QPushButton:hover {
                background-color: #155795;
            }
        """)

        # Create a central container for buttons
        container = QWidget()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Center-align the buttons horizontally
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        container.setLayout(layout)

        # Add a spacer before the buttons to center them
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer_left)

        # Create QPushButton instances for each label
        self.buttons = []
        button_labels = ["Beranda", "Jurnal Log", "Bucket List", "Statistik", "Tambah Lokasi"]
        for label in button_labels:
            button = QPushButton(label)
            layout.addWidget(button)
            self.buttons.append(button)

        # Add a spacer after the buttons to center them
        spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer_right)

        # Add the container to the toolbar
        self.addWidget(container)
