from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from tkinter import Tk, Button as TkButton
from tkcalendar import Calendar  # Import kalender dari tkcalendar
from ..controller.viewJournalController import ViewJournalController
from ..controller.databaseJournalController import DatabaseJournalController
from ..controller.databaseStatisticController import DatabaseStatisticController

class FormJournalPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Variabel flag untuk mencegah pemanggilan ganda
        self.is_saving = False

        # Inisialisasi Controller
        self.db_journal_controller = DatabaseJournalController(db_name="database.db")
        self.db_statistic_controller = DatabaseStatisticController(db_name="database.db")
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

        # Input untuk date dengan Calendar dari tkinter
        self.journal_date_label = Label(text="Date: Not Selected")  # Label untuk menampilkan tanggal
        self.layout.add_widget(self.journal_date_label)

        self.date_picker_button = Button(text="Select Date")  # Tombol untuk membuka kalender
        self.date_picker_button.bind(on_press=self.show_date_picker)
        self.layout.add_widget(self.date_picker_button)

        # Input untuk description (opsional)
        self.journal_description_input = TextInput(hint_text="Enter Description (Optional)", multiline=True)
        self.layout.add_widget(Label(text="Description:"))
        self.layout.add_widget(self.journal_description_input)

        # Tombol Save
        self.save_button = Button(text="Save Journal")
        self.save_button.bind(on_press=self.save_journal)
        self.layout.add_widget(self.save_button)

        self.add_widget(self.layout)

    def show_date_picker(self, instance):
        """
        Tampilkan widget kalender tkinter untuk memilih tanggal.
        """
        def on_date_selected():
            self.selected_date = cal.get_date()  # Ambil tanggal yang dipilih
            self.journal_date_label.text = f"Date: {self.selected_date}"
            root.destroy()  # Tutup jendela tkinter

        root = Tk()  # Buat root tkinter
        root.title("Select Date")
        cal = Calendar(root, date_pattern="yyyy-mm-dd")  # Widget kalender
        cal.pack(pady=60)
        select_button = TkButton(root, text="Select", command=on_date_selected)
        select_button.pack(pady=10)
        root.mainloop()


    def save_journal(self, instance):
        """
        Simpan jurnal baru menggunakan ViewJournalController dan DatabaseJournalController.
        """
        if self.is_saving:
            print("Journal is already being saved. Please wait...")
            return  # Hindari pemanggilan ganda jika sedang proses penyimpanan

        try:
            self.is_saving = True  # Set flag untuk menandakan bahwa penyimpanan sedang dilakukan

            # Ambil input dari form
            title = self.journal_title_input.text.strip()
            country = self.journal_country_input.text.strip()
            city = self.journal_city_input.text.strip()
            date = getattr(self, 'selected_date', None)  # Gunakan tanggal yang dipilih
            description = self.journal_description_input.text.strip() or None

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
            )

            # Simpan jurnal ke database menggunakan DatabaseJournalController
            self.db_journal_controller.save_journal_entry(new_journal)

            # Tambahkan data statistik ke tabel STATISTIC
            print("Updating country visit statistics...")  # Debugging log
            self.db_statistic_controller.update_country_visit_statistics()  # Tambahkan statistik

            # Reset form setelah berhasil menyimpan
            self.journal_title_input.text = ""
            self.journal_country_input.text = ""
            self.journal_city_input.text = ""
            self.journal_date_label.text = "Date: Not Selected"
            self.journal_description_input.text = ""

            print("Journal and statistics saved successfully!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            self.is_saving = False  # Reset flag setelah penyimpanan selesai
