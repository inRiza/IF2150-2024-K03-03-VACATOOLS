from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit,
                             QTextEdit, QFileDialog, QFormLayout, QFrame)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
from img.font.font import FontManager
from src.controller.viewJournalController import JournalController

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit,
                             QTextEdit, QFileDialog, QFormLayout, QFrame)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
from img.font.font import FontManager
from src.controller.viewJournalController import JournalController

class TambahJurnalForm(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = JournalController()  # Inisialisasi controller
        self.gambar_path = None
        self.setup_form()
        

    def setup_form(self):
        """Setup form for adding a new journal entry"""
        font_manager = FontManager()

        form_layout = QFormLayout()

        # Judul input
        self.judul_input = QLineEdit()
        self.judul_input.setPlaceholderText("Masukkan Judul Jurnal")
        form_layout.addRow("Judul:", self.judul_input)

        # Negara dropdown
        self.negara_dropdown = QComboBox()
        self.negara_dropdown.addItems(["Indonesia", "Malaysia", "Singapore"])  # Contoh data
        form_layout.addRow("Negara:", self.negara_dropdown)

        # Kota dropdown
        self.kota_dropdown = QComboBox()
        self.kota_dropdown.addItems(["Jakarta", "Surabaya", "Bandung"])  # Contoh data
        form_layout.addRow("Kota:", self.kota_dropdown)

        # Tanggal input
        self.tanggal_input = QDateEdit(QDate.currentDate())
        self.tanggal_input.setDisplayFormat("dd/MM/yyyy")
        form_layout.addRow("Tanggal:", self.tanggal_input)

        # Deskripsi input
        self.deskripsi_input = QTextEdit()
        form_layout.addRow("Deskripsi:", self.deskripsi_input)

        # Tombol Pilih Gambar
        self.gambar_input_button = QPushButton("Pilih Gambar")
        self.gambar_input_button.clicked.connect(self.choose_image)
        form_layout.addRow("Gambar:", self.gambar_input_button)

        # Label untuk menampilkan gambar yang dipilih
        self.gambar_label = QLabel()
        self.gambar_label.setAlignment(Qt.AlignCenter)
        form_layout.addRow(self.gambar_label)

        # Tombol Submit
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_journal)
        form_layout.addRow(submit_button)

        # Menetapkan layout ke form
        self.setLayout(form_layout)

    def choose_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QPixmap(file_name)
            self.gambar_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
            self.gambar_path = file_name  # Ensure this is set

    def submit_journal(self):
        judul = self.judul_input.text()
        negara = self.negara_dropdown.currentText()
        kota = self.kota_dropdown.currentText()
        tanggal = self.tanggal_input.date().toString("dd/MM/yyyy")
        deskripsi = self.deskripsi_input.toPlainText()

        if not hasattr(self, 'gambar_path') or not self.gambar_path:
            print("No image selected!")
            return

        # Call controller to create a new journal
        self.controller.create_journal(judul, negara, kota, tanggal, deskripsi, self.gambar_path)



        # Reset form setelah submission
        self.judul_input.clear()
        self.negara_dropdown.setCurrentIndex(0)
        self.kota_dropdown.setCurrentIndex(0)
        self.tanggal_input.setDate(QDate.currentDate())
        self.deskripsi_input.clear()
        self.gambar_label.clear()  # Clear image label
        self.gambar_path = None  # Reset image path

        # Optionally, close the form after submission or reset the state
        self.close()



class JournalLogSection(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = JournalController()  # Controller untuk mengakses data jurnal
        self.setup_journal_log_section()

    def setup_journal_log_section(self):
        """Setup content for the journal log section"""
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
        # Menghubungkan tombol dengan fungsi pencarian
        search_button.clicked.connect(lambda: self.handle_search(search_bar.text()))
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
        tambah_jurnal_button.clicked.connect(self.open_tambah_jurnal_form)
        filter_layout.addWidget(tambah_jurnal_button)

        # Add filter layout to the main layout
        main_layout.addLayout(filter_layout)

        # Set the main layout for the journal log section
        self.setLayout(main_layout)

    def handle_search(self, query):
        """Handle search action"""
        result = self.controller.search_journals(query)
        # Tampilkan hasil pencarian di GUI
        for journal in result:
            print(journal)  # Bisa ditampilkan dalam layout, misalnya dengan menambahkan widget baru

    def open_tambah_jurnal_form(self):
        """Open the Add Journal form"""
        self.tambah_jurnal_form = TambahJurnalForm()
        self.tambah_jurnal_form.show()