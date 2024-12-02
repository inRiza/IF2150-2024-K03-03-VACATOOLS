from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QPushButton, QWidget, QHBoxLayout, 
    QSpacerItem, QSizePolicy, QVBoxLayout, QLabel, QStackedWidget, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from src.gui.navbar import Navbar
from src.gui.home_section import HomeSection
from src.gui.journal_log_section import JournalLogSection
from src.gui.bucket_list_section import BucketListSection
from src.gui.stat_section import StatSection

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
        self.bucket_list_section = BucketListSection()
        self.statistic_section = StatSection()
        self.location_section = QWidget()

        # Set up each section
        # self.setup_home_section()
        # self.setup_journal_log_section()
        #self.setup_bucket_list_section()
        #self.setup_statistic_section()
        self.setup_location_section()

        # Add the sections to the stacked widget
        self.central_widget.addWidget(self.home_section)
        self.central_widget.addWidget(self.journal_log_section)
        self.central_widget.addWidget(self.bucket_list_section)
        self.central_widget.addWidget(self.statistic_section)
        self.central_widget.addWidget(self.location_section)

        # Show home section by default
        self.show_home()

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