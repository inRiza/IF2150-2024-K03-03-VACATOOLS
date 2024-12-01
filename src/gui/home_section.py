from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from img.font.font import FontManager  # Import your FontManager

class HomeSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_home_section()

    def setup_home_section(self):
        """Setup content for the home section"""
        # Initialize FontManager
        font_manager = FontManager()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # Adjust spacing between widgets
        main_layout.setContentsMargins(0, 20, 0, 40)  # Remove or adjust outer margin
        
        # Title "Beranda"
        title_label = QLabel("Beranda")
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
        subtitle_label = QLabel("Daftar Jurnal Perjalanan")
        subtitle_label.setFont(font_manager.get_font("regular", 18))  # Use regular font
        subtitle_label.setContentsMargins(20, 0, 0, 5)
        main_layout.addWidget(subtitle_label)

        # Buttons "Buat Jurnal" and "Cari Jurnal"
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignLeft)

        create_button = QPushButton("Buat Jurnal")
        create_button.setStyleSheet(""" 
            QPushButton {
                padding: 10px 5px; 
                margin-bottom: 20px;
                margin-left: 20px;
                background-color: #1c0d52;
                color: white; 
                font-size: 14px; 
                border-radius: 15px;    
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
                border-radius: 15px;    
            }
            QPushButton:hover {
                background-color: #4A86BE;
            }                        
        """)
        search_button.setFixedWidth(150)
        button_layout.addWidget(search_button)

        main_layout.addLayout(button_layout) 

        # Layout for journal cards
        journal_cards_layout = QHBoxLayout()
        journal_cards_layout.setAlignment(Qt.AlignLeft)
        journal_cards_layout.setContentsMargins(20, 0, 0, 0)
        journal_cards_layout.setSpacing(40)

        for _ in range(5):  # Add up to 4 cards
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
            card_title.setFont(font_manager.get_font("bold", 14))  # Use bold font
            card_layout.addWidget(card_title, alignment=Qt.AlignCenter)

            # Card location
            card_location = QLabel("Indonesia - Jakarta")
            card_location.setFont(font_manager.get_font("regular", 12))  # Use regular font
            card_layout.addWidget(card_location, alignment=Qt.AlignCenter)

            # Card date
            card_date = QLabel("24/11/2024")
            card_date.setFont(font_manager.get_font("light", 8))  # Use light font
            card_layout.addWidget(card_date, alignment=Qt.AlignCenter)

            card.setLayout(card_layout)
            journal_cards_layout.addWidget(card)

        # Add journal layout to main layout
        main_layout.addLayout(journal_cards_layout)

        # Set the main layout for the home section
        self.setLayout(main_layout)

        subtitle_label = QLabel("Terakhir Dibuka")
        subtitle_label.setFont(font_manager.get_font("regular", 18))  # Use regular font
        subtitle_label.setContentsMargins(20, 0, 0, 5)
        main_layout.addWidget(subtitle_label)
        
        # Layout for history labels
        history_labels_layout = QHBoxLayout()
        history_labels_layout.setAlignment(Qt.AlignLeft)
        history_labels_layout.setContentsMargins(20, 0, 0, 0)
        history_labels_layout.setSpacing(40)

        for i in range(3):  # Add 3 history labels
            history_label = QLabel("Riwayat Yang DIbuka Oleh Pengguna" + str(i + 1))
            history_label.setFont(font_manager.get_font("regular", 12))
            history_label.setStyleSheet('background-color: #155795; color: white; padding: 10px; border-radius: 8px;')
            history_labels_layout.addWidget(history_label)

        # Add history layout to the main layout
        main_layout.addLayout(history_labels_layout)

        # Stylesheet for cards
        self.setStyleSheet("""
            QWidget#cardJournal {
                background-color: white;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
            }
        """)

