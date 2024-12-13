from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import matplotlib.pyplot as plt
from kivy.uix.image import Image
from kivy.core.window import Window
from io import BytesIO
from ..controller.viewStatisticController import ViewStatisticController
from ..controller.databaseStatisticController import DatabaseStatisticController


class StatisticPage(Screen):
    def __init__(self, db_controller, **kwargs):
        super().__init__(**kwargs)

        # Inisialisasi Controller
        self.statistic_controller = ViewStatisticController(db_controller=db_controller)

        # Tambahkan latar belakang warna putih menggunakan canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Warna putih (RGBA)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # Bind perubahan ukuran dan posisi untuk memperbarui latar belakang
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Tambahkan layout utama
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Tambahkan label judul
        title_label = Label(
            text="Country Visit Statistics",
            color=(0, 0, 0, 1),
            font_size='24sp',
            bold=True,
            halign='center'
        )
        layout.add_widget(title_label)

        # Tambahkan tombol untuk menampilkan chart
        show_chart_button = Button(
            text="Show Statistics Chart",
            size_hint=(1, 0.1)
        )
        show_chart_button.bind(on_press=self.show_statistics_chart)
        layout.add_widget(show_chart_button)

        self.add_widget(layout)

    def _update_bg(self, *args):
        """Perbarui ukuran dan posisi latar belakang."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def show_statistics_chart(self, instance):
        """
        Tampilkan statistik dalam bentuk chart.
        """
        # Ambil data statistik dari controller
        try:
            statistics = self.statistic_controller.get_statistic()
        except Exception as e:
            self.show_popup("Error", f"Failed to fetch statistics: {str(e)}")
            return

        if not statistics:
            self.show_popup("No Data", "No statistics data available!")
            return

        # Hitung jumlah kunjungan per negara
        country_count = {}
        for stat in statistics:
            country_count[stat.country] = country_count.get(stat.country, 0) + stat.total

        if not country_count:
            self.show_popup("No Data", "No statistics data available!")
            return

        # Generate chart menggunakan matplotlib
        countries = list(country_count.keys())
        counts = list(country_count.values())

        plt.figure(figsize=(10, 6))
        plt.bar(countries, counts, color='skyblue')
        plt.title("Number of Visits per Country")
        plt.xlabel("Country")
        plt.ylabel("Visit Count")
        plt.xticks(rotation=45, ha='right')  # Rotasi label untuk keterbacaan
        plt.tight_layout()

        # Simpan chart ke dalam buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        # Tampilkan chart di popup
        self.show_chart_popup(buffer)
        buffer.close()  # Tutup buffer setelah digunakan



    def show_popup(self, title, message):
        """
        Tampilkan popup dengan pesan sederhana.
        """
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message, halign='center')
        close_button = Button(text="Close", size_hint=(1, 0.2))

        layout.add_widget(label)
        layout.add_widget(close_button)

        popup = Popup(title=title, content=layout, size_hint=(0.6, 0.4), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def show_chart_popup(self, buffer):
        """
        Tampilkan chart dalam sebuah popup.
        """
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        chart_image = Image(size_hint=(1, 0.8))
        chart_image.texture = self._load_image_from_buffer(buffer)

        close_button = Button(text="Close", size_hint=(1, 0.2))

        layout.add_widget(chart_image)
        layout.add_widget(close_button)

        popup = Popup(title="Statistics Chart", content=layout, size_hint=(0.9, 0.9), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    @staticmethod
    def _load_image_from_buffer(buffer):
        """
        Convert buffer image to Kivy texture.
        """
        from kivy.core.image import Image as CoreImage
        return CoreImage(BytesIO(buffer.read()), ext="png").texture
