from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from img.font.fontManager import FontManager
from ..controller.databaseBucketListController import DatabaseBucketListController

class BucketViewPage(Screen):
    def __init__(self, bucket_id, **kwargs):
        super().__init__(**kwargs)
        
        # Initialize the database controller and fetch bucket details by ID
        self.db_controller = DatabaseBucketListController("database.db")
        self.bucket_details = self.db_controller.get_bucket_entry_by_id(bucket_id)
        
        self.buc = bucket_id if bucket_id is not None else 'default_value'

        if not self.bucket_details:
            raise ValueError(f"No bucket found with ID {bucket_id}")

        # Add background color using canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color (RGBA)
            self.bg_rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[25])

        # Bind size and position changes to update the background
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Main layout using FloatLayout
        layout = FloatLayout(size=self.size)

        # Title label
        title_label = Label(
            text="bucket Details",
            color=(0, 0, 0, 1),
            font_size='24sp',
            font_name=FontManager.get_font_name("Bold"),
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'x': 0.3, 'y': 0.9}
        )
        layout.add_widget(title_label)

        # Display bucket details
        self.add_detail_label(layout, "Title:", self.bucket_details['title'], 0.75)
        self.add_detail_label(layout, "Country:", self.bucket_details['country'], 0.65)
        self.add_detail_label(layout, "City:", self.bucket_details['city'], 0.55)
        # self.add_detail_label(layout, "Date:", self.bucket_details['date'], 0.45)
        self.add_detail_label(layout, "Description:", self.bucket_details['description'], 0.35, multiline=True)

        # Back button
        back_button = Button(
            text="Back",
            size_hint=(0.2, None),
            height=40,
            pos_hint={'x': 0.4, 'y': 0.1},
            background_color=(0.3, 0.6, 0.9, 1),  # Blue color
            color=(1, 1, 1, 1),  # White text
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),
        )
        back_button.bind(on_release=self.on_back_button_press)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def _update_bg(self, *args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def add_detail_label(self, layout, label_text, value_text, y_position, multiline=False):
        """Helper method to add a detail label to the layout."""
        # Label for the field name
        field_label = Label(
            text=label_text,
            color=(0, 0, 0, 1),
            font_size='18sp',
            font_name=FontManager.get_font_name("Medium"),
            size_hint=(None, None),
            size=(200, 30),
            pos_hint={'x': 0.1, 'y': y_position}
        )
        layout.add_widget(field_label)

        # Label for the field value
        value_label = Label(
            text=value_text,
            color=(0, 0, 0, 1),
            font_size='16sp',
            font_name=FontManager.get_font_name("Regular"),
            size_hint=(None, None),
            size=(600, 30 if not multiline else 100),
            pos_hint={'x': 0.3, 'y': y_position},
            halign='left',
            valign='middle'
        )
        value_label.bind(size=value_label.setter('text_size'))  # Ensure text wraps within bounds
        layout.add_widget(value_label)

    def on_back_button_press(self, instance):
        """Handle the back button press to navigate back to the bucket list."""
        self.manager.current = "BUCKET_LIST"
