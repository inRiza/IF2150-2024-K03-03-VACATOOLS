from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from img.font.fontManager import FontManager  # Import FontManager untuk Poppins
from ..controller.databaseBucketListController import DatabaseBucketListController
import subprocess
import sys

class BucketListPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Initialiaze DatabasebucketController and retrieve bucket entries
        self.db_controller = DatabaseBucketListController("database.db")
        self.bucket_entries = self.db_controller.get_all_bucket_entries()
        
        # Add background color using canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color (RGBA)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # Bind size and position changes to update the background
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Main layout using FloatLayout for fixed positioning
        layout = FloatLayout(size=self.size)

        # Title at the top left
        title_label = Label(
            text="Welcome to Bucket List Page",
            color=(0, 0, 0, 1),
            font_size='24sp',
            font_name=FontManager.get_font_name("Regular"),  # Poppins Regular font
            bold=True,
            halign='left',  # Align the title to the left
            size_hint=(None, None),  # Fixed size
            size=(300, 40)
        )
        title_label.pos = (40, self.height * 6)

        # "Create a bucket" button below the title
        create_button = self.create_button("Create a Bucket List")
        create_button.pos = (20, self.height * 5.5)
        
        create_button.bind(on_press=self.on_create_button_press)

        # Create the bucket container below the button
        bucket_container = self.create_bucket_container()
        bucket_container.pos = (20, self.height * 3.8)

        # Add title, button, and the bucket container to the layout
        layout.add_widget(title_label)
        layout.add_widget(create_button)
        layout.add_widget(bucket_container)

        # Add layout to the screen
        self.add_widget(layout)

    def _update_bg(self, *args):
        """Update the background size and position."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def create_button(self, text):
        """Create a button with a transparent fill and visible rounded border."""
        button = Button(
            text=text,
            size_hint=(0.17, None),  # 60% width, fixed height
            height=40,  # Fixed height
            background_normal='',  # Remove default background
            background_color=(0, 0, 0, 0),  # Transparent background
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),  # Use Poppins Regular
        )

        # Add border with transparent fill
        with button.canvas.before:
            Color(72 / 255, 167 / 255, 215 / 255, 1)  # Border color (blue)
            button.border_rect = RoundedRectangle(
                size=button.size, pos=button.pos, radius=[20]  # Rounded corners
            )

        # Bind to dynamically update the border
        button.bind(size=self._update_border, pos=self._update_border)

        return button

    def _update_border(self, instance, *args):
        """Update the size and position of the border rectangle."""
        instance.border_rect.size = instance.size
        instance.border_rect.pos = instance.pos

    def create_bucket_container(self):
        """Create a container with a scrollable list of buckets."""
        # Create container with specific size and make sure it's centered
        container = FloatLayout(size_hint=(None, None), size=(1100, 450))  # Fixed size
        container.y = self.height * 0.6
        container.x = self.width * 0.2

        # Add a sample background color to the container for visibility
        with container.canvas.before:
            Color(0.9, 0.9, 0.9, 0.6)  # Light grey background color
            RoundedRectangle(size=container.size, pos=container.pos, radius=[25])

        # ScrollView for bucket list
        scroll_view = ScrollView(size_hint=(1, None), height=350)
        scroll_view.y = self.height * 1.5
        scroll_view.x = self.width * 0.2
        container.add_widget(scroll_view)

        # BoxLayout for the bucket list inside ScrollView
        bucket_list_container = BoxLayout(
            orientation='vertical',  # Arrange labels vertically
            size_hint_y=None,
            height=270  # Adjust as needed
        )

        # Sample data (buckets)
        
        for bucket in self.bucket_entries:
        
             # Horizontal BoxLayout for each bucket entry
            bucket_entry_layout = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                spacing=10,
                pos_hint={'x': -0.05},
                height=60  # Fixed height for each entry
            )

            # bucket details label
            bucket_label = Label(
                text=f"{bucket['title']} - {bucket['city']}, {bucket['country']}",
                size_hint_x=0.7,  # Take 70% of the width
                color=(0, 0, 0, 1),
                font_size='14sp',
                font_name=FontManager.get_font_name("Regular"),
            )

            # View button
            view_button = Button(
                text="View",
                size_hint_x=0.15,  # Take 15% of the width
                background_color=(0.3, 0.6, 0.9, 1),  # Blue background
                color=(1, 1, 1, 1),  # White text
                font_size='12sp',
                font_name=FontManager.get_font_name("Regular"),
            )
            view_button.bind(on_release=lambda instance, b=bucket: App.get_running_app().open_bucket_view(b['id']))

            # Delete button
            delete_button = Button(
                text="Delete",
                size_hint_x=0.15,  # Take 15% of the width
                background_color=(0.9, 0.3, 0.3, 1),  # Red background
                color=(1, 1, 1, 1),  # White text
                font_size='12sp',
                font_name=FontManager.get_font_name("Regular"),
            )
            delete_button.bind(on_release=lambda instance, b=bucket: self.on_delete_pressed(b))

            # Add label and buttons to the entry layout
            bucket_entry_layout.add_widget(bucket_label)
            bucket_entry_layout.add_widget(view_button)
            bucket_entry_layout.add_widget(delete_button)

            # Add the bucket entry layout to the list container
            bucket_list_container.add_widget(bucket_entry_layout)

        # Add the bucket list container to the ScrollView
        scroll_view.add_widget(bucket_list_container)

        return container

    def on_view_pressed(self, bucket):
        bucket_id = bucket['id']
        self.manager.current = "VIEW_BUCKET"
        self.manager.get_screen("").__init__(bucket_id)

    def on_delete_pressed(self, bucket):
        """
        Handle tombol delete yang ditekan.
        """
        bucket_id = bucket['id']

        # Hapus data dari database
        self.db_controller.delete_bucket_by_id(bucket_id)
        print(f"Jurnal dengan ID {bucket_id} berhasil dihapus.")

        # Perbarui daftar jurnal di memori
        self.bucket_entries = self.db_controller.get_all_bucket_entries()

        # Schedule restart aplikasi setelah beberapa detik untuk memastikan penghapusan selesai
        Clock.schedule_once(self.restart_app, 0.5)  # Restart setelah 0.5 detik
        
        
    def on_create_button_press(self, instance):
        """Navigate to the FormbucketPage when the button is pressed."""
        self.manager.current = "FORM_BUCKET"
        
    def restart_app(self, dt):
        """Restart aplikasi menggunakan subprocess."""
        print("Aplikasi akan di-restart...")

        # Menghentikan aplikasi
        App.get_running_app().stop()

        # Gunakan subprocess untuk menjalankan ulang aplikasi
        subprocess.Popen([sys.executable, sys.argv[0]])

        # Keluar dari aplikasi yang sedang berjalan
        sys.exit()

