from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class HomeSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_home_section()

    def setup_home_section(self):
        """Setup content for the home section"""
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # Adjust spacing between widgets
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove or adjust outer margins

        # Hero image at the top
        image_label = QLabel()
        pixmap = QPixmap('img/img-hero.png').scaled(1800, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(image_label)

        # Title "Beranda"
        title_label = QLabel("Beranda")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title_label)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("border: 1px solid black; background-color: black;")
        main_layout.addWidget(separator)

        # Subtitle "Daftar Jurnal Perjalanan"
        subtitle_label = QLabel("Daftar Jurnal Perjalanan")
        subtitle_label.setStyleSheet("font-size: 18px;")
        subtitle_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(subtitle_label)

        # Layout for journals and buttons
        journal_layout = QVBoxLayout()

        # Buttons "Buat Jurnal" and "Cari Jurnal"
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignLeft)

        create_button = QPushButton("Buat Jurnal")
        create_button.setStyleSheet("""
            QPushButton {
                padding: 10px 5px; 
                margin-bottom: 20px;
                background-color: white;
                border: 1px solid black; 
                color: black; 
                font-size: 14px; 
                border-radius: 5px;    
            }
            QPushButton:hover {
                background-color: #4A86BE;
                color: white;
            }                            

        """)
        create_button.setFixedWidth(150)
        button_layout.addWidget(create_button)

        search_button = QPushButton("Cari Jurnal")
        search_button.setStyleSheet("""
            QPushButton {
                padding: 10px 5px; 
                margin-bottom: 20px;
                background-color: #1c0d52; 
                color: white; 
                font-size: 14px; 
                border-radius: 5px;    
            }
            QPushButton:hover {
                background-color: #4A86BE;
            }                        
        """)
        search_button.setFixedWidth(150)
        button_layout.addWidget(search_button)

        journal_layout.addLayout(button_layout)

        # Layout for journal cards
        journal_cards_layout = QHBoxLayout()
        journal_cards_layout.setAlignment(Qt.AlignTop)

        for _ in range(4):  # Add up to 4 cards
            card = QWidget()
            card.setObjectName("cardJournal")
            card_layout = QVBoxLayout()
            card_layout.setContentsMargins(10, 10, 10, 10)

            # Card image
            card_image_label = QLabel()
            pixmap = QPixmap("img/img-dummy.png").scaled(120, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            card_image_label.setPixmap(pixmap)
            card_layout.addWidget(card_image_label, alignment=Qt.AlignCenter)

            # Card title
            card_title = QLabel("Jurnal")
            card_title.setStyleSheet("font-size: 14px; font-weight: bold;")
            card_layout.addWidget(card_title, alignment=Qt.AlignLeft)

            # Card location
            card_location = QLabel("Indonesia - Jakarta")
            card_location.setStyleSheet("font-size: 12px; color: gray;")
            card_layout.addWidget(card_location, alignment=Qt.AlignLeft)

            # Card date
            card_date = QLabel("24/11/2024")
            card_date.setStyleSheet("font-size: 12px; color: gray;")
            card_layout.addWidget(card_date, alignment=Qt.AlignLeft)

            card.setLayout(card_layout)
            journal_cards_layout.addWidget(card)

        # Add journal cards layout to journal layout
        journal_layout.addLayout(journal_cards_layout)

        # Add journal layout to main layout
        main_layout.addLayout(journal_layout)

        # Set the main layout for the home section
        self.setLayout(main_layout)

        # Stylesheet for cards
        self.setStyleSheet("""
            QWidget#cardJournal {
                background-color: white;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
                padding: 20px;
                margin-right: 20px; 
                width: 200px;
            }
        """)
