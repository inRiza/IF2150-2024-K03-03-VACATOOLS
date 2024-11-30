from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class JournalLogSection(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_journal_log_section()

    def setup_journal_log_section(self):
        """Setup content for the journal log section"""
        # Main layout for the journal log section
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # Adjust spacing between widgets
        main_layout.setContentsMargins(10, 10, 10, 10)  # Add some outer margins for better spacing

        # Title: "Jurnal Log"
        title_label = QLabel("Jurnal Log")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title_label)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("border: 1px solid black; background-color: black;")
        main_layout.addWidget(separator)

        # Button layout: "Buat Jurnal" and "Cari Jurnal"
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignLeft)

        # "Buat Jurnal" button
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

        # "Cari Jurnal" button
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

        # Add button layout to the main layout
        main_layout.addLayout(button_layout)

        # Journal cards layout
        journal_cards_layout = QHBoxLayout()
        journal_cards_layout.setAlignment(Qt.AlignTop)

        # Create journal cards (maximum 4 for this example)
        for _ in range(4):
            card = QWidget()
            card.setObjectName("cardJournal")
            card_layout = QVBoxLayout()
            card_layout.setContentsMargins(10, 10, 10, 10)

            # Image on the card
            image_label = QLabel()
            pixmap = QPixmap("img/img-dummy.png").scaled(120, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            image_label.setObjectName("cardImage")
            card_layout.addWidget(image_label, alignment=Qt.AlignCenter)

            # Journal title
            title = QLabel("Jurnal")
            title.setObjectName("cardTitle")
            title.setStyleSheet("font-size: 14px; font-weight: bold;")
            card_layout.addWidget(title, alignment=Qt.AlignLeft)

            # Location
            location = QLabel("Indonesia - Jakarta")
            location.setObjectName("cardLocation")
            location.setStyleSheet("font-size: 12px; color: gray;")
            card_layout.addWidget(location, alignment=Qt.AlignLeft)

            # Date
            date = QLabel("24/11/2024")
            date.setObjectName("cardDate")
            date.setStyleSheet("font-size: 12px; color: gray;")
            card_layout.addWidget(date, alignment=Qt.AlignLeft)

            card.setLayout(card_layout)
            journal_cards_layout.addWidget(card)

        # Stylesheet adjustments
        self.setStyleSheet("""
            QWidget#cardJournal {
                background-color: white;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
                padding: 10px;
                width: 200px;
                margin-right: 20px; 
            }
            QLabel#cardImage {
                border: none;
            }
            QLabel#cardTitle {
                font-size: 14px;
                font-weight: bold;
            }
            QLabel#cardLocation, QLabel#cardDate {
                font-size: 12px;
                color: gray;
            }        
        """)

        # Add journal cards layout to the main layout
        main_layout.addLayout(journal_cards_layout)

        # Assign the layout to the journal log section
        self.setLayout(main_layout)
