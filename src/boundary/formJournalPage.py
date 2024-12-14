from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock 
from kivy.uix.spinner import Spinner
from ..controller.viewJournalController import ViewJournalController
from ..controller.databaseJournalController import DatabaseJournalController
from ..controller.databaseStatisticController import DatabaseStatisticController
from ..database.databaseEntity import DatabaseEntity
from tkinter import Tk, Toplevel, Listbox, Button as TkButton 
from tkcalendar import Calendar 
from pathlib import Path


class FormJournalPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_saving = False
        self.locations = []  # Inisialisasi self.locations agar tidak terjadi AttributeError
        db_path = Path(__file__).parent.parent / 'database' / 'database.db'
        # Inisialisasi Controller
        self.db_journal_controller = DatabaseJournalController(db_name="database.db")
        self.db_statistic_controller = DatabaseStatisticController(db_name="database.db")
        self.view_controller = ViewJournalController(db_controller=self.db_journal_controller)
        self.db_entity = DatabaseEntity(db_path=db_path)

        # Layout untuk form
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Input untuk title
        self.journal_title_input = TextInput(hint_text="Enter Journal Title", multiline=False)
        self.layout.add_widget(Label(text="Journal Title:"))
        self.layout.add_widget(self.journal_title_input)

        # Spinner untuk memilih country
        self.layout.add_widget(Label(text="Country:"))
        self.country_spinner = Spinner(
            text='Select Country',
            values=[],  # Akan diupdate dengan data negara
            size_hint=(None, None),
            size=(200, 44)
        )
        self.country_spinner.bind(text=self.on_country_select)
        self.layout.add_widget(self.country_spinner)

        # Spinner untuk memilih city
        self.layout.add_widget(Label(text="City:"))
        self.city_spinner = Spinner(
            text='Select City',
            values=[],  # Akan diupdate dengan data kota
            size_hint=(None, None),
            size=(200, 44)
        )
        self.layout.add_widget(self.city_spinner)

        # Input untuk date
        self.journal_date_label = Label(text="Date: Not Selected")
        self.layout.add_widget(self.journal_date_label)

        self.date_picker_button = Button(text="Select Date")
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

        # Load data untuk dropdown
        self.load_location_data()

    def load_location_data(self):
        """
        Load data untuk country dan city dari tabel LOCATION.
        """
        try:
            location_data = self.db_entity.getData("LOCATION", "country", "city")
            if not location_data:
                print("No locations found in the database.")
                return

            # Mengubah data mentah menjadi objek LocationEntity
            self.locations = [{"country": row["country"], "city": row["city"]} for row in location_data]
            print(f"Processed locations: {self.locations}")  # Debugging log

            # Memperbarui UI setelah data dimuat
            Clock.schedule_once(self.update_ui, 0)
        except Exception as e:
            print(f"Error loading location data: {e}")
            self.locations = []

    def update_ui(self, dt):
        """
        Memperbarui UI setelah data locations dimuat.
        """
        print(f"Updating UI with {len(self.locations)} locations.")
        if not self.locations:
            print("No locations available to update the UI.")
            return

        # Mengupdate spinner untuk country dengan nilai yang ada di self.locations
        countries = sorted({loc["country"] for loc in self.locations})
        self.country_spinner.values = countries  # Mengupdate pilihan country pada spinner
        if countries:
            self.country_spinner.text = countries[0]  # Menampilkan country pertama sebagai default


    def on_country_select(self, spinner, text):
        """
        Handle selection of country from Spinner.
        Update the cities dropdown based on selected country.
        """
        print(f"Selected country: {text}")
        if not text or text == "Select Country":
            print("Please select a valid country.")
            return

        cities = sorted({loc["city"] for loc in self.locations if loc["country"] == text})
        if not cities:
            print(f"No cities found for the country: {text}.")
            return

        # Update city spinner with cities from selected country
        self.city_spinner.values = cities
        self.city_spinner.text = "Select City"  # Reset city spinner text

    def show_date_picker(self, instance):
        """
        Tampilkan widget kalender tkinter untuk memilih tanggal.
        """
        def on_date_selected():
            self.selected_date = cal.get_date()
            self.journal_date_label.text = f"Date: {self.selected_date}"
            root.destroy()

        root = Tk()
        root.title("Select Date")
        cal = Calendar(root, date_pattern="yyyy-mm-dd")
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
            return

        try:
            self.is_saving = True

            title = self.journal_title_input.text.strip()
            country = self.country_spinner.text.strip()
            city = self.city_spinner.text.strip()
            date = getattr(self, 'selected_date', None)
            description = self.journal_description_input.text.strip() or None

            # Validate the inputs
            self.view_controller.validate_input(
                ['title', 'country', 'city', 'date'],
                title=title, country=country, city=city, date=date
            )

            # Create a new journal object
            new_journal = self.view_controller.create_journal(
                title=title,
                country=country,
                city=city,
                date=date,
                description=description,
            )

            # Save the journal to the database
            self.db_journal_controller.save_journal(new_journal)
            
            # Tambahkan data statistik ke tabel STATISTIC
            print("Updating country visit statistics...")  # Debugging log
            self.db_statistic_controller.update_country_visit_statistics()  # Update statistics

            # Reset form after saving successfully
            self.journal_title_input.text = ""
            self.country_spinner.text = 'Select Country'
            self.city_spinner.text = 'Select City'
            self.journal_date_label.text = "Date: Not Selected"
            self.journal_description_input.text = ""

            print("Journal and statistics saved successfully!")

            self.is_saving = False
            print("Journal saved successfully.")

        except Exception as e:
            print(f"Error saving journal: {e}")
            self.is_saving = False
