import os
from PyQt5.QtGui import QFontDatabase, QFont

class FontManager:
    def __init__(self):
        self.fonts = {}
        self.load_fonts()

    def load_fonts(self):
        """Load custom fonts with different weights and styles."""
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        font_files = {
            "bold": "Satoshi-Bold.otf",
            "light": "Satoshi-Light.otf",
            "regular": "Satoshi-Regular.otf",
            "italic": "Satoshi-Italic.otf",
            "bold_italic": "Satoshi-BoldItalic.otf",
            "medium": "Satoshi-Medium.otf",
            "medium_italic": "Satoshi-MediumItalic.otf",
            "light_italic": "Satoshi-LightItalic.otf",
        }

        for style, filename in font_files.items():
            font_path = os.path.join(script_dir, filename)  # Construct full path
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id != -1:
                self.fonts[style] = QFontDatabase.applicationFontFamilies(font_id)[0]
            else:
                print(f"Failed to load font: {font_path}")

    def get_font(self, style: str, size: int):
        """
        Get a QFont instance for a specific style.
        
        :param style: Font style (e.g., "bold", "regular", "italic").
        :param size: Font size.
        :return: QFont object.
        """
        font_family = self.fonts.get(style, "Arial")  # Fallback to Arial if style not found
        return QFont(font_family, size)
