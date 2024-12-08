# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
# from PyQt5.QtCore import Qt
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# from img.font.font import FontManager
# from src.database.database import get_statistics_data  # Import data source

# class StatSection(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.data = get_statistics_data()  # Retrieve data from database.py
#         self.setup_statistic_section()

#     def setup_statistic_section(self):
#         """Setup content for the statistic section."""
#         # Initialize FontManager
#         font_manager = FontManager()

#         # Main layout
#         main_layout = QVBoxLayout()
#         main_layout.setSpacing(10)
#         main_layout.setContentsMargins(20, 20, 20, 20)

#         # Title: Statistik
#         title_label = QLabel("Statistik")
#         title_label.setFont(font_manager.get_font("bold", 24))
#         title_label.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(title_label)

#         # Separator
#         separator = QFrame()
#         separator.setFrameShape(QFrame.HLine)
#         separator.setStyleSheet("border: 2px solid gray; background-color: black;")
#         main_layout.addWidget(separator)

#         # Subtitle
#         subtitle_label = QLabel("Jumlah Kunjungan Berdasarkan Negara/Kota")
#         subtitle_label.setFont(font_manager.get_font("regular", 18))
#         subtitle_label.setAlignment(Qt.AlignLeft)
#         main_layout.addWidget(subtitle_label)

#         # Chart Widget
#         chart = self.create_bar_chart()
#         main_layout.addWidget(chart)

#         # Set the layout to the widget
#         self.setLayout(main_layout)

#     def create_bar_chart(self):
#         """Create a bar chart using Matplotlib."""
#         figure = Figure()
#         canvas = FigureCanvas(figure)
#         ax = figure.add_subplot(111)

#         # Data for the chart
#         locations = list(self.data.keys())
#         visit_counts = list(self.data.values())

#         # Create bar chart
#         ax.bar(locations, visit_counts, color="#4A86BE")
#         ax.set_title("Jumlah Kunjungan per Negara/Kota", fontsize=14)
#         ax.set_xlabel("Negara/Kota", fontsize=12)
#         ax.set_ylabel("Jumlah Kunjungan", fontsize=12)
#         ax.set_xticks(range(len(locations)))
#         ax.set_xticklabels(locations, rotation=45, ha="right")

#         # Add grid for better readability
#         ax.grid(axis="y", linestyle="--", alpha=0.7)

#         return canvas
