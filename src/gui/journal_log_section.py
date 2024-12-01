from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QFrame
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from img.font.font import FontManager  # Import your FontManager


class JournalLogSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_journal_log_section()

    def setup_journal_log_section(self):
        """Setup content for the journal log section"""
        # Initialize FontManager
        font_manager = FontManager()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        main_layout.setContentsMargins(0, 20, 0, 40)

        # Title "Beranda"
        title_label = QLabel("Jurnal Log")
        title_label.setFont(font_manager.get_font("bold", 24))  # Use bold font
        title_label.setContentsMargins(10, 0, 0, 0)
        title_label.setAlignment(Qt.AlignTop)
        main_layout.addWidget(title_label)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("border: 3px solid gray; background-color: black;")
        separator.setFixedWidth(int(self.width() * 2.1))  # Set width as 80% of the parent widget's width
        main_layout.addWidget(separator, alignment=Qt.AlignHCenter)

        # Subtitle "Daftar Jurnal Perjalanan"
        subtitle_label = QLabel("Lakukan Pencarian")
        subtitle_label.setFont(font_manager.get_font("regular", 18))  # Use regular font
        subtitle_label.setContentsMargins(20, 0, 0, 5)
        main_layout.addWidget(subtitle_label)
        
        # Search Bar and Filter Layout
        filter_layout = QHBoxLayout()
        filter_layout.setSpacing(10)
        filter_layout.setContentsMargins(20, 0, 20, 100)
        filter_layout.setAlignment(Qt.AlignLeft)

        # Search Bar
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Cari Judul...")
        search_bar.setStyleSheet("padding: 10px; font-size: 12px; border: 1px solid gray; border-radius: 15px;")
        search_bar.setFixedWidth(500)
        filter_layout.addWidget(search_bar)

        # Search Button
        search_button = QPushButton("Cari")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #1c0d52;
                color: white;
                padding: 10px 5px;
                font-size: 14px;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #4A86BE;
            }
        """)
        search_button.setFixedWidth(100)
        filter_layout.addWidget(search_button)

        # Dropdown Filter
        filter_dropdown = QComboBox()
        filter_dropdown.addItems(["Filter by Negara", "Indonesia"])
        filter_dropdown.setStyleSheet("padding: 10px; font-size: 12px; border: 1px solid gray; border-radius: 15px;")
        filter_dropdown.setFixedWidth(150)
        filter_layout.addWidget(filter_dropdown)

        # Tambah Jurnal Button
        tambah_jurnal_button = QPushButton("Tambah Jurnal")
        tambah_jurnal_button.setStyleSheet("""
            QPushButton {
                background-color: #1c0d52;
                color: white;
                padding: 10px 5px;
                font-size: 14px;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #4A86BE;
            }
        """)
        tambah_jurnal_button.setFixedWidth(150)
        filter_layout.addWidget(tambah_jurnal_button)

        # Add filter layout to the main layout
        main_layout.addLayout(filter_layout)

        # Layout for journal cards
        journal_cards_layout = QHBoxLayout()
        journal_cards_layout.setAlignment(Qt.AlignCenter)
        journal_cards_layout.setSpacing(50)

        for _ in range(6):  # max 6
            card = QWidget()
            card.setObjectName("cardJournal")
            card_layout = QVBoxLayout()

            # Card image
            card_image_label = QLabel()
            pixmap = QPixmap("img/img-dummy.png").scaled(120, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            card_image_label.setPixmap(pixmap)
            card_layout.addWidget(card_image_label, alignment=Qt.AlignCenter)

            # Card title
            card_title = QLabel("Jurnal")
            card_title.setFont(font_manager.get_font("bold", 14))
            card_layout.addWidget(card_title, alignment=Qt.AlignCenter)

            # Card location
            card_location = QLabel("Indonesia - Jakarta")
            card_location.setFont(font_manager.get_font("regular", 12))
            card_layout.addWidget(card_location, alignment=Qt.AlignCenter)

            # Card date
            card_date = QLabel("01/12/2024")
            card_date.setFont(font_manager.get_font("light", 10))
            card_layout.addWidget(card_date, alignment=Qt.AlignCenter)

            card.setLayout(card_layout)
            journal_cards_layout.addWidget(card)

        # Add journal cards layout to the main layout
        main_layout.addLayout(journal_cards_layout)

        # Set the main layout for the journal log section
        self.setLayout(main_layout)
        
        # Layout for journal cards
        journal_cards_layout = QHBoxLayout()
        journal_cards_layout.setAlignment(Qt.AlignCenter)
        journal_cards_layout.setSpacing(50)

        for _ in range(6):  # max 6
            card = QWidget()
            card.setObjectName("cardJournal")
            card_layout = QVBoxLayout()

            # Card image
            card_image_label = QLabel()
            pixmap = QPixmap("img/img-dummy.png").scaled(120, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            card_image_label.setPixmap(pixmap)
            card_layout.addWidget(card_image_label, alignment=Qt.AlignCenter)

            # Card title
            card_title = QLabel("Jurnal")
            card_title.setFont(font_manager.get_font("bold", 14))
            card_layout.addWidget(card_title, alignment=Qt.AlignCenter)

            # Card location
            card_location = QLabel("Indonesia - Jakarta")
            card_location.setFont(font_manager.get_font("regular", 12))
            card_layout.addWidget(card_location, alignment=Qt.AlignCenter)

            # Card date
            card_date = QLabel("01/12/2024")
            card_date.setFont(font_manager.get_font("light", 10))
            card_layout.addWidget(card_date, alignment=Qt.AlignCenter)

            card.setLayout(card_layout)
            journal_cards_layout.addWidget(card)

        # Add journal cards layout to the main layout
        main_layout.addLayout(journal_cards_layout)

        # Set the main layout for the journal log section
        self.setLayout(main_layout)

        # Stylesheet for cards
        self.setStyleSheet("""
            QWidget#cardJournal {
                background-color: white;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
                padding: 10px;
            }
        """)