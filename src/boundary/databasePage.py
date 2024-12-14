from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from pathlib import Path
from ..database.databaseEntity import DatabaseEntity  # Impor DatabaseEntity

class DatabasePage(Screen):
    def __init__(self, db_entity: DatabaseEntity, **kwargs):
        super().__init__(**kwargs)
        
        # Tentukan path lengkap untuk file database.db
        db_path = Path(__file__).parent.parent/'database'/'database.db'

        # Buat instance DatabaseEntity dengan path yang benar
        self.db_entity = DatabaseEntity(db_path=str(db_path))  # Berikan path yang benar ke DatabaseEntity

        # Tambahkan latar belakang warna putih menggunakan canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Warna putih (RGBA)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # Bind perubahan ukuran dan posisi untuk memperbarui latar belakang
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Layout utama
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Tambahkan input untuk Country dan City
        self.country_input = TextInput(hint_text="Enter Country", multiline=False)
        self.city_input = TextInput(hint_text="Enter City", multiline=False)

        # Tambahkan tombol untuk menambah data
        add_button = Button(text="Add Location", on_press=self.add_location)

        # Label untuk status
        self.status_label = Label(text="", color=(0, 0, 0, 1), halign='center')

        # Container untuk menampilkan data dari database
        self.data_container = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.data_container.bind(minimum_height=self.data_container.setter('height'))

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.data_container)

        # Tambahkan widget ke layout utama
        self.main_layout.add_widget(Label(text="Add Location", color=(0, 0, 0, 1), font_size='20sp', bold=True, halign='center'))
        self.main_layout.add_widget(self.country_input)
        self.main_layout.add_widget(self.city_input)
        self.main_layout.add_widget(add_button)
        self.main_layout.add_widget(self.status_label)
        self.main_layout.add_widget(Label(text="Locations in Database:", color=(0, 0, 0, 1), font_size='16sp', bold=True))
        self.main_layout.add_widget(scroll_view)

        self.add_widget(self.main_layout)

        # Muat data dari database ke container
        self.load_data()

    def _update_bg(self, *args):
        """Perbarui ukuran dan posisi latar belakang."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def add_location(self, instance):
        """Tambahkan lokasi baru ke database."""
        country = self.country_input.text.strip()
        city = self.city_input.text.strip()

        if not country or not city:
            self.status_label.text = "Both fields are required."
            return
        
        try:
            # Tambahkan data ke tabel LOCATION
            self.db_entity.addData('LOCATION', country=country, city=city)
            self.status_label.text = "Location added successfully."
            self.country_input.text = ""
            self.city_input.text = ""
            
            # Perbarui data di container
            self.load_data()
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

    def load_data(self):
        """Muat data dari tabel LOCATION ke dalam container."""
        # Hapus semua widget sebelumnya
        self.data_container.clear_widgets()

        try:
            data = self.db_entity.getData('LOCATION', 'country', 'city')

            for entry in data:
                country = entry['country']
                city = entry['city']

                # Layout untuk setiap item data
                item_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)

                # Label untuk menampilkan data
                item_label = Label(text=f"{country}, {city}", color=(0, 0, 0, 1), halign='left')

                # Tombol untuk menghapus data
                delete_button = Button(text="Delete", size_hint_x=None, width=100)
                delete_button.bind(on_press=lambda btn, c=country, ci=city: self.delete_location(c, ci))

                # Tambahkan widget ke layout item
                item_layout.add_widget(item_label)
                item_layout.add_widget(delete_button)

                # Tambahkan layout item ke container
                self.data_container.add_widget(item_layout)

        except Exception as e:
            self.status_label.text = f"Error loading data: {str(e)}"

    def delete_location(self, country, city):
        """Hapus lokasi dari database."""
        try:
            query = "DELETE FROM LOCATION WHERE country = ? AND city = ?"
            self.db_entity.cursor.execute(query, (country, city))
            self.db_entity.conn.commit()

            self.status_label.text = "Location deleted successfully."

            # Perbarui data di container
            self.load_data()
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
