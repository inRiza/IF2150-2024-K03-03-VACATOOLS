from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from ..controller.viewJournalController import ViewJournalController
from ..controller.databaseJournalController import DatabaseJournalController

class FormJournalPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Inisialisasi DatabaseJournalController dan ViewJournalController
        self.db_journal_controller = DatabaseJournalController(db_name="database.db")
        self.view_controller = ViewJournalController(db_controller=self.db_journal_controller)

        # Layout untuk form
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Input untuk title
        self.journal_title_input = TextInput(hint_text="Enter Journal Title", multiline=False)
        self.layout.add_widget(Label(text="Journal Title:"))
        self.layout.add_widget(self.journal_title_input)

        # Input untuk country
        self.journal_country_input = TextInput(hint_text="Enter Country", multiline=False)
        self.layout.add_widget(Label(text="Country:"))
        self.layout.add_widget(self.journal_country_input)

        # Input untuk city
        self.journal_city_input = TextInput(hint_text="Enter City", multiline=False)
        self.layout.add_widget(Label(text="City:"))
        self.layout.add_widget(self.journal_city_input)

        # Input untuk date
        self.journal_date_input = TextInput(hint_text="Enter Date (YYYY-MM-DD)", multiline=False)
        self.layout.add_widget(Label(text="Date:"))
        self.layout.add_widget(self.journal_date_input)

        # Input untuk description (opsional)
        self.journal_description_input = TextInput(hint_text="Enter Description (Optional)", multiline=True)
        self.layout.add_widget(Label(text="Description:"))
        self.layout.add_widget(self.journal_description_input)

        # Input untuk memilih image (opsional)
        self.image_path_input = TextInput(hint_text="Select Image (Optional)", multiline=False, readonly=True)
        self.layout.add_widget(Label(text="Image Path:"))
        self.layout.add_widget(self.image_path_input)

        # Tombol untuk membuka file chooser
        self.select_image_button = Button(text="Choose Image")
        self.select_image_button.bind(on_press=self.select_image)
        self.layout.add_widget(self.select_image_button)

        # Tombol Save
        self.save_button = Button(text="Save Journal")
        self.save_button.bind(on_press=self.save_journal)  # Hubungkan tombol ke fungsi
        self.layout.add_widget(self.save_button)

        self.add_widget(self.layout)

    def select_image(self, instance):
        """
        Fungsi untuk membuka file chooser dan memilih gambar.
        """
        file_chooser = FileChooserIconView()
        file_chooser.filters = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']  # Menambahkan filter gambar
        file_chooser.bind(on_selection=self.on_file_select)

        # Buat popup dan tampilkan file chooser di dalamnya
        popup = Popup(title="Select Image", content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

    def on_file_select(self, instance, selection):
        """
        Menangani pemilihan file gambar.
        """
        if selection:
            self.image_path_input.text = selection[0]  # Ambil path file yang dipilih
            instance.parent.parent.dismiss()  # Menutup popup setelah file dipilih
        else:
            self.image_path_input.text = ""

    def save_journal(self, instance):
        """
        Simpan jurnal baru menggunakan ViewJournalController dan DatabaseJournalController.
        """
        try:
            # Ambil input dari form
            title = self.journal_title_input.text.strip()
            country = self.journal_country_input.text.strip()
            city = self.journal_city_input.text.strip()
            date = self.journal_date_input.text.strip()
            description = self.journal_description_input.text.strip() or None
            image_path = self.image_path_input.text.strip() or None  # Menambahkan image_path

            # Validasi input menggunakan ViewJournalController
            self.view_controller.validate_input(
                ['title', 'country', 'city', 'date'],
                title=title, country=country, city=city, date=date
            )

            # Buat jurnal baru menggunakan ViewJournalController
            new_journal = self.view_controller.create_journal(
                title=title,
                country=country,
                city=city,
                date=date,
                description=description,
                image_path=image_path  # Menambahkan image_path
            )

            # Simpan jurnal ke database menggunakan DatabaseJournalController
            self.db_journal_controller.save_journal_entry(new_journal)

            # Reset form setelah berhasil menyimpan
            self.journal_title_input.text = ""
            self.journal_country_input.text = ""
            self.journal_city_input.text = ""
            self.journal_date_input.text = ""
            self.journal_description_input.text = ""
            self.image_path_input.text = ""  # Reset image path

            # Tampilkan popup dan berpindah ke page lain
            self.show_success_popup()

            print("Journal saved successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def show_success_popup(self):
        print("Masuk ke fungsi show_success_popup")  # Debug log
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text="Journal has been created")
        close_button = Button(text="OK", size_hint=(1, 0.2))

        layout.add_widget(label)
        layout.add_widget(close_button)

        popup = Popup(title="Success", content=layout, size_hint=(0.6, 0.4), auto_dismiss=False)

        def on_close(instance):
            print("Popup ditutup, pindah ke JOURNAL_LOG")  # Debug log
            popup.dismiss()
            self.manager.current = "JOURNAL_LOG"  # Pindah ke layar lain

        close_button.bind(on_press=on_close)

        try:
            popup.open()
            print("Popup berhasil dibuka")  # Debug log
        except Exception as e:
            print(f"Error membuka popup: {e}")  # Jika ada error
            
    def reset_form(self):
        self.journal_title_input.text = ""
        self.journal_country_input.text = ""
        self.journal_city_input.text = ""
        self.journal_date_input.text = ""
        self.journal_description_input.text = ""
        self.image_path_input.text = ""


