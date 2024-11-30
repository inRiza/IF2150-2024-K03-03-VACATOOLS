from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QPushButton, QWidget, QHBoxLayout, 
    QSpacerItem, QSizePolicy, QVBoxLayout, QLabel, QStackedWidget, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from src.gui.navbar import Navbar
from src.gui.home_section import HomeSection
from src.gui.journal_log_section import JournalLogSection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VACATOOLS")

        # Set the window size
        self.setGeometry(200, 200, 300, 300)

        # Navbar
        self.navbar = Navbar(self)
        self.addToolBar(Qt.TopToolBarArea, self.navbar)

        # Connect buttons to respective section functions
        self.navbar.buttons[0].clicked.connect(self.show_home)
        self.navbar.buttons[1].clicked.connect(self.show_journal_log)
        self.navbar.buttons[2].clicked.connect(self.show_bucket_list)
        self.navbar.buttons[3].clicked.connect(self.show_statistic)
        self.navbar.buttons[4].clicked.connect(self.show_location)

        # Create the central widget for the main content area (QStackedWidget for dynamic content change)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Create sections
        self.home_section = HomeSection()
        self.journal_log_section = JournalLogSection()
        self.bucket_list_section = QWidget()
        self.statistic_section = QWidget()
        self.location_section = QWidget()

        # Set up each section
        # self.setup_home_section()
        # self.setup_journal_log_section()
        self.setup_bucket_list_section()
        self.setup_statistic_section()
        self.setup_location_section()

        # Add the sections to the stacked widget
        self.central_widget.addWidget(self.home_section)
        self.central_widget.addWidget(self.journal_log_section)
        self.central_widget.addWidget(self.bucket_list_section)
        self.central_widget.addWidget(self.statistic_section)
        self.central_widget.addWidget(self.location_section)

        # Show home section by default
        self.show_home()

    # def setup_home_section(self):
    #     """Setup content for the home section"""
    #     main_layout = QVBoxLayout()
    #     main_layout.setSpacing(10)  # Adjust spacing between widgets
    #     main_layout.setContentsMargins(0, 0, 0, 0)  # Remove or adjust outer margins

    #     # Hero image at the top
    #     image_label = QLabel()
    #     pixmap = QPixmap('assets/img-hero.png').scaled(1800, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #     image_label.setPixmap(pixmap)
    #     image_label.setAlignment(Qt.AlignCenter)
    #     main_layout.addWidget(image_label)

    #     # Title "Beranda"
    #     title_label = QLabel("Beranda")
    #     title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
    #     title_label.setAlignment(Qt.AlignLeft)
    #     main_layout.addWidget(title_label)

    #     # Separator
    #     separator = QFrame()
    #     separator.setFrameShape(QFrame.HLine)
    #     separator.setStyleSheet("border: 1px solid black; background-color: black;")
    #     main_layout.addWidget(separator)

    #     # Subtitle "Daftar Jurnal Perjalanan"
    #     subtitle_label = QLabel("Daftar Jurnal Perjalanan")
    #     subtitle_label.setStyleSheet("font-size: 18px;")
    #     subtitle_label.setAlignment(Qt.AlignLeft)
    #     main_layout.addWidget(subtitle_label)

    #     # Layout for journals and buttons
    #     journal_layout = QVBoxLayout()

    #     # Buttons "Buat Jurnal" and "Cari Jurnal"
    #     button_layout = QHBoxLayout()
    #     button_layout.setAlignment(Qt.AlignLeft)

    #     create_button = QPushButton("Buat Jurnal")
    #     create_button.setStyleSheet("""
    #         QPushButton {
    #             padding: 10px 5px; 
    #             margin-bottom: 20px;
    #             background-color: white;
    #             border: 1px solid black; 
    #             color: black; 
    #             font-size: 14px; 
    #             border-radius: 5px;    
    #         }
    #         QPushButton:hover {
    #             background-color: #4A86BE;
    #             color: white;
    #         }                            
    #     """)
    #     create_button.setFixedWidth(150)
    #     button_layout.addWidget(create_button)

    #     search_button = QPushButton("Cari Jurnal")
    #     search_button.setStyleSheet("""
    #         QPushButton {
    #             padding: 10px 5px; 
    #             margin-bottom: 20px;
    #             background-color: #1c0d52; 
    #             color: white; 
    #             font-size: 14px; 
    #             border-radius: 5px;    
    #         }
    #         QPushButton:hover {
    #             background-color: #4A86BE;
    #         }                        
    #     """)
    #     search_button.setFixedWidth(150)
    #     button_layout.addWidget(search_button)

    #     journal_layout.addLayout(button_layout)

    #     # Layout for journal cards
    #     journal_cards_layout = QHBoxLayout()
    #     journal_cards_layout.setAlignment(Qt.AlignTop)

    #     for _ in range(4):  # Add up to 4 cards
    #         card = QWidget()
    #         card.setObjectName("cardJournal")
    #         card_layout = QVBoxLayout()
    #         card_layout.setContentsMargins(10, 10, 10, 10)

    #         # Card image
    #         card_image_label = QLabel()
    #         pixmap = QPixmap("assets/img-dummy.png").scaled(120, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #         card_image_label.setPixmap(pixmap)
    #         card_layout.addWidget(card_image_label, alignment=Qt.AlignCenter)

    #         # Card title
    #         card_title = QLabel("Jurnal")
    #         card_title.setStyleSheet("font-size: 14px; font-weight: bold;")
    #         card_layout.addWidget(card_title, alignment=Qt.AlignLeft)

    #         # Card location
    #         card_location = QLabel("Indonesia - Jakarta")
    #         card_location.setStyleSheet("font-size: 12px; color: gray;")
    #         card_layout.addWidget(card_location, alignment=Qt.AlignLeft)

    #         # Card date
    #         card_date = QLabel("24/11/2024")
    #         card_date.setStyleSheet("font-size: 12px; color: gray;")
    #         card_layout.addWidget(card_date, alignment=Qt.AlignLeft)

    #         card.setLayout(card_layout)
    #         journal_cards_layout.addWidget(card)

    #     # Add journal cards layout to journal layout
    #     journal_layout.addLayout(journal_cards_layout)

    #     # Add journal layout to main layout
    #     main_layout.addLayout(journal_layout)

    #     # Set the main layout for the home section
    #     self.home_section.setLayout(main_layout)

    #     # Stylesheet for cards
    #     app.setStyleSheet("""
    #         QWidget#cardJournal {
    #             background-color: white;
    #             border: 1px solid #dcdcdc;
    #             border-radius: 8px;
    #             padding: 20px;
    #             margin-right: 20px; 
    #             width: 200px;
    #         }
    #     """)

        
    # def setup_journal_log_section(self):
    #     """Setup content for the journal log section"""
    #     # Main layout for the journal log section
    #     main_layout = QVBoxLayout()
    #     main_layout.setSpacing(10)  # Adjust spacing between widgets
    #     main_layout.setContentsMargins(10, 10, 10, 10)  # Add some outer margins for better spacing

    #     # Title: "Jurnal Log"
    #     title_label = QLabel("Jurnal Log")
    #     title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
    #     title_label.setAlignment(Qt.AlignLeft)
    #     main_layout.addWidget(title_label)

    #     # Separator
    #     separator = QFrame()
    #     separator.setFrameShape(QFrame.HLine)
    #     separator.setStyleSheet("border: 1px solid black; background-color: black;")
    #     main_layout.addWidget(separator)

    #     # Button layout: "Buat Jurnal" and "Cari Jurnal"
    #     button_layout = QHBoxLayout()
    #     button_layout.setAlignment(Qt.AlignLeft)

    #     # "Buat Jurnal" button
    #     create_button = QPushButton("Buat Jurnal")
    #     create_button.setStyleSheet("""
    #         QPushButton {
    #             padding: 10px 5px; 
    #             margin-bottom: 20px;
    #             background-color: white;
    #             border: 1px solid black; 
    #             color: black; 
    #             font-size: 14px; 
    #             border-radius: 5px;    
    #         }
    #         QPushButton:hover {
    #             background-color: #4A86BE;
    #             color: white;
    #         }                            
    #     """)
    #     create_button.setFixedWidth(150)
    #     button_layout.addWidget(create_button)

    #     # "Cari Jurnal" button
    #     search_button = QPushButton("Cari Jurnal")
    #     search_button.setStyleSheet("""
    #         QPushButton {
    #             padding: 10px 5px; 
    #             margin-bottom: 20px;
    #             background-color: #1c0d52; 
    #             color: white; 
    #             font-size: 14px; 
    #             border-radius: 5px;    
    #         }
    #         QPushButton:hover {
    #             background-color: #4A86BE;
    #         }                        
    #     """)
    #     search_button.setFixedWidth(150)
    #     button_layout.addWidget(search_button)

    #     # Add button layout to the main layout
    #     main_layout.addLayout(button_layout)

    #     # Journal cards layout
    #     journal_cards_layout = QHBoxLayout()
    #     journal_cards_layout.setAlignment(Qt.AlignTop)

    #     # Create journal cards (maximum 4 for this example)
    #     for _ in range(4):
    #         card = QWidget()
    #         card.setObjectName("cardJournal")
    #         card_layout = QVBoxLayout()
    #         card_layout.setContentsMargins(10, 10, 10, 10)

    #         # Image on the card
    #         image_label = QLabel()
    #         pixmap = QPixmap("assets/img-dummy.png").scaled(120, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #         image_label.setPixmap(pixmap)
    #         image_label.setObjectName("cardImage")
    #         card_layout.addWidget(image_label, alignment=Qt.AlignCenter)

    #         # Journal title
    #         title = QLabel("Jurnal")
    #         title.setObjectName("cardTitle")
    #         title.setStyleSheet("font-size: 14px; font-weight: bold;")
    #         card_layout.addWidget(title, alignment=Qt.AlignLeft)

    #         # Location
    #         location = QLabel("Indonesia - Jakarta")
    #         location.setObjectName("cardLocation")
    #         location.setStyleSheet("font-size: 12px; color: gray;")
    #         card_layout.addWidget(location, alignment=Qt.AlignLeft)

    #         # Date
    #         date = QLabel("24/11/2024")
    #         date.setObjectName("cardDate")
    #         date.setStyleSheet("font-size: 12px; color: gray;")
    #         card_layout.addWidget(date, alignment=Qt.AlignLeft)

    #         card.setLayout(card_layout)
    #         journal_cards_layout.addWidget(card)

    #     # Stylesheet adjustments
    #     self.setStyleSheet("""
    #         QWidget#cardJournal {
    #             background-color: white;
    #             border: 1px solid #dcdcdc;
    #             border-radius: 8px;
    #             padding: 10px;
    #             width: 200px;
    #             margin-right: 20px; 
    #         }
    #         QLabel#cardImage {
    #             border: none;
    #         }
    #         QLabel#cardTitle {
    #             font-size: 14px;
    #             font-weight: bold;
    #         }
    #         QLabel#cardLocation, QLabel#cardDate {
    #             font-size: 12px;
    #             color: gray;
    #         }        
    #     """)

    #     # Add journal cards layout to the main layout
    #     main_layout.addLayout(journal_cards_layout)

    #     # Assign the layout to the journal log section
    #     self.journal_log_section = QWidget()
    #     self.journal_log_section.setLayout(main_layout)

    def setup_bucket_list_section(self):
        """Setup content for the bucket list section"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the Bucket List Section!"))
        self.bucket_list_section.setLayout(layout)

    def setup_statistic_section(self):
        """Setup content for the statistic section"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the Statistic Section!"))
        self.statistic_section.setLayout(layout)

    def setup_location_section(self):
        """Setup content for the location section"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the Location Section!"))
        self.location_section.setLayout(layout)

    def show_home(self):
        """Show the home section"""
        self.central_widget.setCurrentWidget(self.home_section)
        self.setWindowTitle("VACATOOLS - Beranda")

    def show_journal_log(self):
        """Show the journal log section"""
        self.central_widget.setCurrentWidget(self.journal_log_section)
        self.setWindowTitle("VACATOOLS - Jurnal Log")

    def show_bucket_list(self):
        """Show the bucket list section"""
        self.central_widget.setCurrentWidget(self.bucket_list_section)
        self.setWindowTitle("VACATOOLS - Bucket List")

    def show_statistic(self):
        """Show the statistic section"""
        self.central_widget.setCurrentWidget(self.statistic_section)
        self.setWindowTitle("VACATOOLS - Statistik")

    def show_location(self):
        """Show the location section"""
        self.central_widget.setCurrentWidget(self.location_section)
        self.setWindowTitle("VACATOOLS - Tambah Lokasi")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())