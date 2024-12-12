from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.filechooser import FileChooserIconView
from img.font.fontManager import FontManager
from datetime import datetime
from ..controller.viewJournalController import ViewJournalController  # Import the controller
from ..database.databaseEntity import DatabaseEntity

class FormJournalPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view_controller = ViewJournalController(DatabaseEntity)  # Initialize controller

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
            text="Create a New Journal",
            color=(0, 0, 0, 1),
            font_size='24sp',
            font_name=FontManager.get_font_name("Regular"),  # Poppins Regular font
            bold=True,
            size_hint=(None, None),
            size=(300, 40)
        )
        title_label.pos = (20, self.height * 7)

        # Journal Title Input
        self.journal_title_input = TextInput(
            hint_text="Enter Journal Title (Max 250 characters)",
            size_hint=(0.8, None),
            height=40,
            font_name=FontManager.get_font_name("Regular"),
        )
        self.journal_title_input.pos = (self.width * 0.1, self.height * 6.5)

        # Country Spinner (dropdown)
        self.country_spinner = Spinner(
            text="Select Country",
            values=("USA", "France", "Japan", "Italy"),
            size_hint=(None, None),
            size=(200, 40),
            font_name=FontManager.get_font_name("Regular"),
        )
        self.country_spinner.pos = (self.width * 0.1, self.height * 5.8)

        # City Spinner (dropdown)
        self.city_spinner = Spinner(
            text="Select City",
            values=("New York", "Paris", "Tokyo", "Rome"),
            size_hint=(None, None),
            size=(200, 40),
            font_name=FontManager.get_font_name("Regular"),
        )
        self.city_spinner.pos = (self.width * 0.1, self.height * 5.2)

        # Description Input
        self.description_input = TextInput(
            hint_text="Enter Journal Description (Max 800 words)",
            size_hint=(0.8, None),
            height=200,
            multiline=True,
            font_name=FontManager.get_font_name("Regular"),
        )
        self.description_input.pos = (self.width * 0.1, self.height * 2.5)

        # Image Selection Button
        self.image_button = Button(
            text="Select Image",
            size_hint=(None, None),
            size=(200, 40),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),
        )
        self.image_button.pos = (self.width * 0.1, self.height * 2)
        self.image_button.bind(on_release=self.on_select_image)

        # Date Picker Button
        self.date_button = Button(
            text="Select Date",
            size_hint=(None, None),
            size=(200, 40),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),
        )
        self.date_button.pos = (self.width * 0.1, self.height * 1.5)
        self.date_button.bind(on_release=self.show_date_picker)

        # Save Button
        save_button = Button(
            text="Save Journal",
            size_hint=(None, None),
            size=(400, 40),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),
        )
        save_button.pos = (self.width * 0.1, self.height * 0.5)
        save_button.bind(on_release=self.save_journal)

        # Add all widgets to the layout
        layout.add_widget(title_label)
        layout.add_widget(self.journal_title_input)
        layout.add_widget(self.country_spinner)
        layout.add_widget(self.city_spinner)
        layout.add_widget(self.description_input)
        layout.add_widget(self.image_button)
        layout.add_widget(self.date_button)  # Add Date Button
        layout.add_widget(save_button)

        # Add layout to the screen
        self.add_widget(layout)

    def save_journal(self, instance):
        """Handle save action"""
        journal_data = {
            "title": self.journal_title_input.text,
            "country": self.country_spinner.text,
            "city": self.city_spinner.text,
            "description": self.description_input.text,
            "image_path": getattr(self, "selected_image_path", ""),
            "date": self.date_button.text.split(": ")[1]
        }
        
        # Pass the journal data to the controller
        self.view_controller.create_journal(journal_data)

    def _update_bg(self, *args):
        """Update the background size and position."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def on_select_image(self, instance):
        """Handle image selection."""
        # Create the file chooser without the 'title' property
        filechooser = FileChooserIconView(filters=["*.jpg", "*.png"], multiselect=False)
        filechooser.bind(on_submit=self.on_image_selected)

        # Create a Popup for the FileChooser with a title in the Popup, not the FileChooser
        popup = Popup(
            title="Choose an Image",
            content=filechooser,
            size_hint=(0.8, 0.8)
        )
        popup.open()

    def on_image_selected(self, filechooser, selection, *args):
        """Handle the file selected from the file chooser."""
        if selection:
            selected_file = selection[0]  # Get the file path
            self.image_button.text = f"Selected: {selected_file.split('/')[-1]}"  # Update button text with the selected image filename

            # Optionally, you can store the file path if needed
            self.selected_image_path = selected_file
        else:
            self.image_button.text = "No file selected"

    def show_date_picker(self, instance):
        """Show the date picker using Spinners for day, month, and year."""
        date_popup_content = BoxLayout(orientation='vertical')

        # Create Spinners for day, month, and year
        self.day_spinner = Spinner(
            text="Day",
            values=[str(i) for i in range(1, 32)],
            size_hint=(None, None),
            size=(100, 40),
            font_name=FontManager.get_font_name("Regular"),
        )
        self.month_spinner = Spinner(
            text="Month",
            values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            size_hint=(None, None),
            size=(150, 40),
            font_name=FontManager.get_font_name("Regular"),
        )
        self.year_spinner = Spinner(
            text="Year",
            values=[str(i) for i in range(datetime.now().year - 10, datetime.now().year + 1)],
            size_hint=(None, None),
            size=(100, 40),
            font_name=FontManager.get_font_name("Regular"),
        )

        date_popup_content.add_widget(self.day_spinner)
        date_popup_content.add_widget(self.month_spinner)
        date_popup_content.add_widget(self.year_spinner)

        # Create Confirm Button
        confirm_button = Button(
            text="Confirm Date",
            size_hint=(None, None),
            size=(200, 40),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size='14sp',
            font_name=FontManager.get_font_name("Regular"),
        )
        confirm_button.bind(on_release=self.on_date_selected)
        date_popup_content.add_widget(confirm_button)

        # Create the popup
        date_popup = Popup(
            title="Select Date",
            content=date_popup_content,
            size_hint=(0.8, 0.8),
        )
        date_popup.open()

    def on_date_selected(self, instance):
        """Handle the selected date and display it on the date button."""
        selected_day = self.day_spinner.text
        selected_month = self.month_spinner.text
        selected_year = self.year_spinner.text

        # Combine the date
        selected_date = f"{selected_day} {selected_month} {selected_year}"

        # Update the date button text to show the selected date
        self.date_button.text = f"Selected Date: {selected_date}"
