from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
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
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Tambahkan input untuk Country dan City
        self.country_input = TextInput(hint_text="Enter Country", multiline=False)
        self.city_input = TextInput(hint_text="Enter City", multiline=False)

        # Tambahkan tombol untuk menambah data
        add_button = Button(text="Add Location", on_press=self.add_location)

        # Label untuk status
        self.status_label = Label(text="", color=(0, 0, 0, 1), halign='center')

        # Tambahkan widget ke layout
        layout.add_widget(Label(text="Add Location", color=(0, 0, 0, 1), font_size='20sp', bold=True, halign='center'))
        layout.add_widget(self.country_input)
        layout.add_widget(self.city_input)
        layout.add_widget(add_button)
        layout.add_widget(self.status_label)

        self.add_widget(layout)

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
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
