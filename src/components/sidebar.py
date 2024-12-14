from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.app import App
from img.font.fontManager import FontManager
import sys
import subprocess

class Sidebar(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (0.2, 1)
        self.spacing = 10
        self.padding = [10, 20]  # Padding kiri-kanan, atas-bawah

        # Latar belakang sidebar dengan gradien halus
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
            
            # Tambahkan gradien
            self.gradients = []
            num_steps = 50
            for i in range(num_steps):
                ratio = i / float(num_steps - 1)
                start_color = (72 / 255, 167 / 255, 215 / 255)
                end_color = (31 / 255, 42 / 255, 171 / 255)
                color = (
                    start_color[0] * (1 - ratio) + end_color[0] * ratio,
                    start_color[1] * (1 - ratio) + end_color[1] * ratio,
                    start_color[2] * (1 - ratio) + end_color[2] * ratio,
                    1
                )
                Color(*color)
                rect_height = self.height / num_steps
                rect_pos = (self.x, self.y + self.height - (i + 1) * rect_height)
                rect = Rectangle(size=(self.width, rect_height), pos=rect_pos)
                self.gradients.append(rect)

        self.bind(pos=self._update_bg, size=self._update_bg)

        # Pusatkan tombol secara vertikal
        self.center_layout = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=10)
        self.center_layout.bind(minimum_height=self.center_layout.setter('height'))
        self.add_widget(Widget())  # Spacer di atas
        self.add_widget(self.center_layout)
        self.add_widget(Widget())  # Spacer di bawah

        # Tambahkan tombol navigasi
        buttons = [
            {"text": "Home", "screen_name": "HOME"},
            {"text": "Journal Log", "screen_name": "JOURNAL_LOG"},
            {"text": "Bucket List", "screen_name": "BUCKET_LIST"},
            {"text": "Statistic", "screen_name": "STATISTIC"},
            {"text": "Location", "screen_name": "LOCATION"},
        ]

        for button_data in buttons:
            self.center_layout.add_widget(self.create_button(screen_manager, button_data))

        # Tambahkan tombol Reload
        reload_button = Button(
            text="Reload",
            size_hint=(1, None),
            height=50,
            background_normal='',  # Hilangkan tampilan normal agar latar belakang terlihat
            background_color=(0, 0, 0, 0),  # Transparan untuk menggunakan latar gradien
            font_name=FontManager.get_font_name("Regular"),  # Set font Poppins Regular
            color=(1, 1, 1, 1),  # Optional: Set text color to white for visibility
        )
        reload_button.bind(on_release=self.restart_app)
        self.center_layout.add_widget(reload_button)

    def create_button(self, screen_manager, button_data):
        """Membuat tombol dengan teks saja."""
        button = Button(
            text=button_data['text'],
            size_hint=(1, None),
            height=50,
            background_normal='',  # Hilangkan tampilan normal agar latar belakang terlihat
            background_color=(0, 0, 0, 0),  # Transparan untuk menggunakan latar gradien
            font_name=FontManager.get_font_name("Regular"),  # Set font Poppins Regular
            color=(1, 1, 1, 1),  # Optional: Set text color to white for visibility
        )
        # Bind aksi tombol ke fungsi navigasi
        button.bind(on_release=lambda btn: self.switch_screen(screen_manager, button_data['screen_name']))
        return button

    def _update_bg(self, *args):
        """Perbarui ukuran dan posisi latar belakang."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos
        for i, rect in enumerate(self.gradients):
            rect.size = (self.width, self.height / len(self.gradients))
            rect.pos = (self.x, self.y + self.height - (i + 1) * rect.size[1])

    def switch_screen(self, screen_manager, screen_name):
        """Navigasi ke layar tertentu."""
        if screen_name in screen_manager.screen_names:
            screen_manager.current = screen_name

    def restart_app(self, dt=None):
        """Restart aplikasi menggunakan subprocess."""
        print("Aplikasi akan di-restart...")

        # Menghentikan aplikasi
        App.get_running_app().stop()

        # Gunakan subprocess untuk menjalankan ulang aplikasi
        subprocess.Popen([sys.executable, sys.argv[0]])

        # Keluar dari aplikasi yang sedang berjalan
        sys.exit()
