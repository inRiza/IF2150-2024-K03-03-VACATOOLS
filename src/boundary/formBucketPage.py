from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
# from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from img.font.fontManager import FontManager


class FormBucketPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add background color using canvas.before
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color (RGBA)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # Bind size and position changes to update the background
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Main layout using FloatLayout for fixed positioning
        layout = FloatLayout(size=self.size)

        # Title
        title_label = Label(
            text="Create a New bucket",
            color=(0, 0, 0, 1),
            font_size='24sp',
            font_name=FontManager.get_font_name("Regular"),  # Poppins Regular font
            bold=True,
            size_hint=(None, None),
            size=(300, 40)
        )
        title_label.pos = (20, self.height * 7)

        # bucket Title Input
        bucket_title_input = TextInput(
            hint_text="Enter bucket Title (Max 250 characters)",
            size_hint=(0.8, None),
            height=40,
            font_name=FontManager.get_font_name("Regular"),
        )
        bucket_title_input.pos = (self.width * 0.1, self.height * 6.5)

        # Country Spinner (dropdown)
        country_spinner = Spinner(
            text="Select Country",
            values=("USA", "France", "Japan", "Italy"),
            size_hint=(None, None),
            size=(200, 40),
            font_name=FontManager.get_font_name("Regular"),
        )
        country_spinner.pos = (self.width * 0.1, self.height * 5.8)

        # City Spinner (dropdown)
        city_spinner = Spinner(
            text="Select City",
            values=("New York", "Paris", "Tokyo", "Rome"),
            size_hint=(None, None),
            size=(200, 40),
            font_name=FontManager.get_font_name("Regular"),
        )
        city_spinner.pos = (self.width * 0.1, self.height * 5.2)

        # Description Input
        description_input = TextInput(
            hint_text="Enter bucket Description (Max 800 words)",
            size_hint=(0.8, None),
            height=200,
            multiline=True,
            font_name=FontManager.get_font_name("Regular"),
        )
        description_input.pos = (self.width * 0.1, self.height * 2.5)

        # # Image Selection Button
        # self.image_button = Button(
        #     text="Select Image",
        #     size_hint=(None, None),
        #     size=(200, 40),
        #     background_color=(0.3, 0.6, 0.9, 1),
        #     color=(1, 1, 1, 1),
        #     font_size='14sp',
        #     font_name=FontManager.get_font_name("Regular"),
        # )
        # self.image_button.pos = (self.width * 0.1, self.height * 1.5)
        # self.image_button.bind(on_release=self.on_select_image)

        # Save Button
        save_button = Button(
            text="Save bucket",
            size_hint=(None, None),
            size=(200, 40),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),
        )
        save_button.pos = (self.width * 0.1, self.height * 0.5)

        # Add all widgets to the layout
        layout.add_widget(title_label)
        layout.add_widget(bucket_title_input)
        layout.add_widget(country_spinner)
        layout.add_widget(city_spinner)
        layout.add_widget(description_input)
        # layout.add_widget(self.image_button)
        layout.add_widget(save_button)

        # Add layout to the screen
        self.add_widget(layout)

    def _update_bg(self, *args):
        """Update the background size and position."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    # def on_select_image(self, instance):
    #     """Handle image selection."""
    #     # Create the file chooser without the 'title' property
    #     filechooser = FileChooserIconView(filters=["*.jpg", "*.png"], multiselect=False)
    #     filechooser.bind(on_submit=self.on_image_selected)

    #     # Create a Popup for the FileChooser with a title in the Popup, not the FileChooser
    #     popup = Popup(
    #         title="Choose an Image",
    #         content=filechooser,
    #         size_hint=(0.8, 0.8)
    #     )
    #     popup.open()

    # def on_image_selected(self, filechooser, selection, *args):
    #     """Handle the file selected from the file chooser."""
    #     if selection:
    #         selected_file = selection[0]  # Get the file path
    #         self.image_button.text = f"Selected: {selected_file.split('/')[-1]}"  # Update button text with the selected image filename

    #         # Optionally, you can store the file path if needed
    #         self.selected_image_path = selected_file
    #     else:
    #         self.image_button.text = "No file selected"
