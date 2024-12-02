from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from img.font.font import FontManager

class BucketListSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_bucket_list_section()

    def setup_bucket_list_section(self):
        """Setup content for the bucket list section"""
        # Initialize FontManager
        font_manager = FontManager()

        # Main layout for the bucket list section
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title: Bucket List
        title_label = QLabel("Bucket List")
        title_label.setFont(font_manager.get_font("bold", 24))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("border: 2px solid gray; background-color: black;")
        main_layout.addWidget(separator)

        # Add Button
        add_button = QPushButton("Tambah")
        add_button.setStyleSheet("""
            QPushButton {
                padding: 10px 15px; 
                background-color: #1c0d52; 
                color: white; 
                font-size: 16px; 
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #4A86BE;
            }
        """)
        add_button.setFixedWidth(120)
        add_button.setFixedHeight(40)
        main_layout.addWidget(add_button, alignment=Qt.AlignCenter)

        # Cards Section
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(20)
        cards_layout.setAlignment(Qt.AlignLeft)

        # Add Dummy Cards
        for i in range(3):  # Add 3 dummy cards
            card = QWidget()
            card.setObjectName("bucketCard")
            card_layout = QVBoxLayout()
            card_layout.setSpacing(10)

            # Card Title
            card_title = QLabel(f"Bucket List {i + 1}")
            card_title.setFont(font_manager.get_font("bold", 14))
            card_title.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(card_title)

            # Card Location
            card_location = QLabel(f"Lokasi: Negara {['Jepang', 'Swiss', 'Italia'][i]}")
            card_location.setFont(font_manager.get_font("regular", 12))
            card_location.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(card_location)

            card.setLayout(card_layout)
            cards_layout.addWidget(card)

        # Add cards layout to the main layout
        main_layout.addLayout(cards_layout)

        # Apply layout to the widget
        self.setLayout(main_layout)

        # Stylesheet for the cards
        self.setStyleSheet("""
            QWidget#bucketCard {
                background-color: #f9f9f9;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
                padding: 10px;
                min-width: 150px;
                max-width: 200px;
            }
        """)
