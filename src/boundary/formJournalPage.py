from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock  # Pastikan Clock digunakan untuk update UI
from tkinter import Tk, Toplevel, Listbox, Button as TkButton, SINGLE
from tkcalendar import Calendar  # Tambahkan impor Calendar dari tkcalendar
from ..controller.viewJournalController import ViewJournalController
from ..controller.databaseJournalController import DatabaseJournalController
from ..controller.databaseStatisticController import DatabaseStatisticController
from ..database.databaseEntity import DatabaseEntity


class FormJournalPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_saving = False
        self.locations = []  # Inisialisasi self.locations agar tidak terjadi AttributeError

        # Inisialisasi Controller
        self.db_journal_controller = DatabaseJournalController(db_name="database.db")
        self.db_statistic_controller = DatabaseStatisticController(db_name="database.db")
        self.view_controller = ViewJournalController(db_controller=self.db_journal_controller)
        self.db_entity = DatabaseEntity(db_path="database.db")

        # Layout untuk form
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Input untuk title
        self.journal_title_input = TextInput(hint_text="Enter Journal Title", multiline=False)
        self.layout.add_widget(Label(text="Journal Title:"))
        self.layout.add_widget(self.journal_title_input)

        # Tombol untuk memilih country
        self.layout.add_widget(Label(text="Country:"))
        self.country_button = Button(text="Select Country")
        self.country_button.bind(on_press=self.show_country_picker)
        self.layout.add_widget(self.country_button)

        # Tombol untuk memilih city
        self.layout.add_widget(Label(text="City:"))
        self.city_button = Button(text="Select City")
        self.city_button.bind(on_press=self.show_city_picker)
        self.layout.add_widget(self.city_button)

        # Input untuk date dengan Calendar dari tkinter
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
            locations = self.db_entity.getData("LOCATION", "country", "city")
            print(f"Fetched locations from database: {locations}")  # Debugging log
            if not locations:
                print("No locations found in the database.")
                return
            self.locations = [{"country": row["country"], "city": row["city"]} for row in locations]
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
        
        # Memanggil show_country_picker untuk memperbarui dropdown
        self.show_country_picker(None)  # Panggil untuk memperbarui dropdown country

    def show_country_picker(self, instance):
        """
        Menampilkan daftar country dari data yang diambil langsung lewat DatabaseEntity.
        """
        if not self.locations:
            print("No locations loaded. Ensure database is set up correctly.")
            return

        countries = sorted({loc["country"] for loc in self.locations})
        if not countries:
            print("No countries found.")
            return

        def on_select():
            selected = listbox.get(listbox.curselection())
            self.country_button.text = selected
            self.city_button.text = "Select City"
            popup.destroy()

        popup = Toplevel()
        popup.title("Select Country")
        popup.geometry("300x400")

        listbox = Listbox(popup, selectmode=SINGLE, height=20)
        for country in countries:
            print(f"Inserting country: {country}")  # Debugging log
            listbox.insert("end", country)
        listbox.pack(pady=10)

        select_button = TkButton(popup, text="Select", command=on_select)
        select_button.pack(pady=10)

    def show_city_picker(self, instance):
        """
        Menampilkan daftar city berdasarkan country yang dipilih.
        """
        selected_country = self.country_button.text
        if not selected_country or selected_country == "Select Country":
            print("Please select a country first.")
            return

        cities = sorted({loc["city"] for loc in self.locations if loc["country"] == selected_country})
        if not cities:
            print(f"No cities found for the country: {selected_country}.")
            return

        def on_select():
            selected = listbox.get(listbox.curselection())
            self.city_button.text = selected
            popup.destroy()

        popup = Toplevel()
        popup.title("Select City")
        popup.geometry("300x400")

        listbox = Listbox(popup, selectmode=SINGLE, height=20)
        for city in cities:
            print(f"Inserting city: {city}")  # Debugging log
            listbox.insert("end", city)
        listbox.pack(pady=10)

        select_button = TkButton(popup, text="Select", command=on_select)
        select_button.pack(pady=10)

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
            country = self.country_button.text.strip()
            city = self.city_button.text.strip()
            date = getattr(self, 'selected_date', None)
            description = self.journal_description_input.text.strip() or None

            self.view_controller.validate_input(
                ['title', 'country', 'city', 'date'],
                title=title, country=country, city=city, date=date
            )

            new_journal = self.view_controller.create_journal(
                title=title,
                country=country,
                city=city,
                date=date,
                description=description,
            )

            self.db_journal_controller.save_journal_entry(new_journal)
            self.db_statistic_controller.update_country_visit_statistics()

            self.journal_title_input.text = ""
            self.country_button.text = "Select Country"
            self.city_button.text = "Select City"
            self.journal_date_label.text = "Date: Not Selected"
            self.journal_description_input.text = ""

            print("Journal and statistics saved successfully!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            self.is_saving = False

