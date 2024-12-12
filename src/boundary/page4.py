from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class Page4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Tambahkan latar belakang warna putih menggunakan canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Warna putih (RGBA)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # Bind perubahan ukuran dan posisi untuk memperbarui latar belakang
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Tambahkan konten ke layar
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(
            text="This is Page 4",
            color = (0, 0, 0, 1),
            font_size='24sp',
            bold=True,
            halign='center'
        ))
        self.add_widget(layout)

    def _update_bg(self, *args):
        """Perbarui ukuran dan posisi latar belakang."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos
