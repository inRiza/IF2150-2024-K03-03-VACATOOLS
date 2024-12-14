from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from ..controller.viewBucketListController import ViewBucketListController
from ..controller.databaseBucketListController import DatabaseBucketListController

class FormBucketPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Inisialisasi DatabasebucketController dan ViewbucketController
        self.db_bucket_controller =DatabaseBucketListController(db_name="database.db")
        self.view_controller = ViewBucketListController(db_controller=self.db_bucket_controller)

        # Layout untuk form
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Input untuk title
        self.bucket_title_input = TextInput(hint_text="Enter bucket Title", multiline=False)
        self.layout.add_widget(Label(text="bucket Title:"))
        self.layout.add_widget(self.bucket_title_input)

        # Input untuk country
        self.bucket_country_input = TextInput(hint_text="Enter Country", multiline=False)
        self.layout.add_widget(Label(text="Country:"))
        self.layout.add_widget(self.bucket_country_input)

        # Input untuk city
        self.bucket_city_input = TextInput(hint_text="Enter City", multiline=False)
        self.layout.add_widget(Label(text="City:"))
        self.layout.add_widget(self.bucket_city_input)

        # # Input untuk date
        # self.bucket_date_input = TextInput(hint_text="Enter Date (YYYY-MM-DD)", multiline=False)
        # self.layout.add_widget(Label(text="Date:"))
        # self.layout.add_widget(self.bucket_date_input)

        # Input untuk description (opsional)
        self.bucket_description_input = TextInput(hint_text="Enter Description (Optional)", multiline=True)
        self.layout.add_widget(Label(text="Description:"))
        self.layout.add_widget(self.bucket_description_input)

        # # Input untuk memilih image (opsional)
        # self.image_path_input = TextInput(hint_text="Select Image (Optional)", multiline=False, readonly=True)
        # self.layout.add_widget(Label(text="Image Path:"))
        # self.layout.add_widget(self.image_path_input)

        # # Tombol untuk membuka file chooser
        # self.select_image_button = Button(text="Choose Image")
        # self.select_image_button.bind(on_press=self.select_image)
        # self.layout.add_widget(self.select_image_button)

        # Tombol Save
        self.save_button = Button(text="Save bucket")
        self.save_button.bind(on_press=self.save_bucket)  # Hubungkan tombol ke fungsi
        self.layout.add_widget(self.save_button)

        self.add_widget(self.layout)

    # def select_image(self, instance):
    #     """
    #     Fungsi untuk membuka file chooser dan memilih gambar.
    #     """
    #     file_chooser = FileChooserIconView()
    #     file_chooser.filters = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']  # Menambahkan filter gambar
    #     file_chooser.bind(on_selection=self.on_file_select)

    #     # Buat popup dan tampilkan file chooser di dalamnya
    #     popup = Popup(title="Select Image", content=file_chooser, size_hint=(0.9, 0.9))
    #     popup.open()

    # def on_file_select(self, instance, selection):
    #     """
    #     Menangani pemilihan file gambar.
    #     """
    #     if selection:
    #         self.image_path_input.text = selection[0]  # Ambil path file yang dipilih
    #         instance.parent.parent.dismiss()  # Menutup popup setelah file dipilih
    #     else:
    #         self.image_path_input.text = ""

    
    def save_bucket(self, instance):
        """
        Simpan jurnal baru menggunakan ViewbucketController dan DatabasebucketController.
        """
        try:
            # Ambil input dari form
            title = self.bucket_title_input.text.strip()
            country = self.bucket_country_input.text.strip()
            city = self.bucket_city_input.text.strip()
            # date = self.bucket_date_input.text.strip()
            description = self.bucket_description_input.text.strip() or None
            # image_path = self.image_path_input.text.strip() or None  # Menambahkan image_path

            # Buat jurnal baru menggunakan ViewbucketController
            self.view_controller.validate_input(
                ['title', 'country', 'city'],
                title=title, country=country, city=city
            )

            new_bucket = self.view_controller.create_bucket(
                title=title,
                country=country,
                city=city,
                # date=date,
                description=description
                # image_path=image_path  # Menambahkan image_path
            )

            # Simpan jurnal ke database menggunakan DatabasebucketController
            self.db_bucket_controller.save_bucket_entry(new_bucket)

            # Reset form setelah berhasil menyimpan
            self.bucket_title_input.text = ""
            self.bucket_country_input.text = ""
            self.bucket_city_input.text = ""
            # self.bucket_date_input.text = ""
            self.bucket_description_input.text = ""
            # self.image_path_input.text = ""  # Reset image path

            print("bucket saved successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
