from kivy.core.text import LabelBase
import os

class FontManager:
    @staticmethod
    def register_fonts():
        # Get the absolute path to the fonts directory
        fonts_dir = os.path.dirname(__file__)  # This is the folder where fontManager.py is located

        LabelBase.register(
            name="PoppinsRegular",
            fn_regular=os.path.join(fonts_dir, "Poppins-Regular.ttf")
        )
        LabelBase.register(
            name="PoppinsBold",
            fn_regular=os.path.join(fonts_dir, "Poppins-Bold.ttf")
        )
        LabelBase.register(
            name="PoppinsMedium",
            fn_regular=os.path.join(fonts_dir, "Poppins-Medium.ttf")
        )
        LabelBase.register(
            name="PoppinsLight",
            fn_regular=os.path.join(fonts_dir, "Poppins-Light.ttf")
        )

    @staticmethod
    def get_font_name(style="Regular"):
        font_styles = {
            "Regular": "PoppinsRegular",
            "Bold": "PoppinsBold",
            "Medium": "PoppinsMedium",
            "Light": "PoppinsLight",
        }
        return font_styles.get(style, "PoppinsRegular")  # Default to Regular if not found
