from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.image import Image  # Import Image widget
from kivy.uix.floatlayout import FloatLayout
from img.font.fontManager import FontManager # Import FontManager untuk Poppins

class HomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Daftarkan font Poppins
        FontManager.register_fonts()

        # Latar belakang dengan warna putih
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Perbarui ukuran latar belakang saat ukuran layar berubah
        self.bind(size=self._update_bg, pos=self._update_bg)

        # FloatLayout untuk teks dan gambar
        main_layout = FloatLayout(size_hint=(1, 1))

        # Title Section
        title = Label(
            text="Welcome to VACATOOLS",
            font_size='24sp',
            bold=True,
            halign='center',
            color=(0, 0, 0, 1),  # Teks hitam
            font_name=FontManager.get_font_name("Bold"),  # Gunakan Poppins Bold
            size_hint=(None, None),
            size=(300, 50),  # Ukuran tetap untuk label
            pos_hint={'center_x': 0.5, 'top': 0.9}  # Posisikan di tengah atas
        )
        main_layout.add_widget(title)

        # Second Label Section
        subtitle = Label(
            text="Create your travel stories",
            font_size='18sp',
            halign='center',
            color=(0, 0, 0, 1),  # Teks hitam
            font_name=FontManager.get_font_name("Regular"), 
            size_hint=(None, None),
            size=(300, 50),  # Ukuran tetap untuk subtitle
            pos_hint={'center_x': 0.5, 'top': 0.85}  # Posisikan di bawah judul
        )
        main_layout.add_widget(subtitle)

        # Placeholder for Image Section - Ganti dengan gambar
        image_placeholder = FloatLayout(size_hint=(1, None), height=350)  # FloatLayout untuk gambar
        image = Image(source='img/vacation_illustration.png', size_hint=(None, None), size=(500, 400))
        image.pos_hint = {'center_x': 0.5} 
        image.y = self.height * 2  # Gambar akan berada di bawah teks
        image_placeholder.add_widget(image)
        main_layout.add_widget(image_placeholder)

        # Buttons Section
        buttons_layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            size_hint=(0.5, None),
            height=160,  # Tinggi total layout untuk 3 tombol
            pos_hint={"center_x": 0.5}  # Pusatkan tombol secara horizontal
        )

        # Tambahkan tombol dengan desain baru
        buttons_layout.add_widget(self.create_button("Journal Log"))
        buttons_layout.add_widget(self.create_button("Bucket List"))
        buttons_layout.add_widget(self.create_button("Check Statistic"))
        
        buttons_layout.padding = [20, 0, 0, 80]  # Menambahkan padding bawah

        main_layout.add_widget(buttons_layout)

        self.add_widget(main_layout)

    def _update_bg(self, *args):
        """Perbarui ukuran dan posisi latar belakang saat ukuran layar berubah."""
        self.rect.size = self.size
        self.rect.pos = self.pos

    def create_button(self, text):
        """Create a button with a transparent fill and a visible rounded border."""
        button = Button(
            text=text,
            size_hint=(0.4, None),  # 40% width of layout, fixed height
            height=40,  # Fixed button height
            pos_hint={"center_x": 0.5},  # Center the button horizontally
            background_normal='',  # Remove the default background image
            background_color=(0, 0, 0, 0),  # Transparent background
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),  # Gunakan Poppins Regular
        )

        # Tambahkan border dengan RoundedRectangle
        with button.canvas.before:
            Color(72 / 255, 167 / 255, 215 / 255, 1)  # Border color (blue)
            button.border_rect = RoundedRectangle(
                size=button.size, pos=button.pos, radius=[20]  # Rounded corners
            )

        # Bind to update the border dynamically when button size or position changes
        button.bind(size=self._update_border, pos=self._update_border)

        # Tambahkan aksi pada tombol
        if text == "Journal Log":
            button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'JOURNAL_LOG'))
        elif text == "Bucket List":
            button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'BUCKET_LIST'))
        elif text == "Check Statistic":
            button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'STATISTIC'))

        return button


    def _update_border(self, instance, *args):
        """Update the size and position of the border rectangle dynamically."""
        instance.border_rect.size = instance.size
        instance.border_rect.pos = instance.pos
