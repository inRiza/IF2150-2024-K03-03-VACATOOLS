from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.graphics import Color, Rectangle
from src.components.sidebar import Sidebar
from src.boundary.homePage import HomePage
from src.boundary.journalPage import JournalPage
from src.boundary.bucketListPage import BucketListPage
from src.boundary.statisticPage import StatisticPage
from src.boundary.databasePage import DatabasePage
from src.boundary.formJournalPage import FormJournalPage  
from src.boundary.formBucketPage import FormBucketPage 
from src.controller.databaseStatisticController import DatabaseStatisticController  
from src.database.databaseEntity import DatabaseEntity  # Tambahkan impor DatabaseEntity

class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')

        # Membuat instance db_controller (DatabaseStatisticController)
        db_controller = DatabaseStatisticController("database.db")
        db_entity = DatabaseEntity("database.db")  # Membuat instance DatabaseEntity

        # Screen manager to handle navigation
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomePage(name='HOME'))
        screen_manager.add_widget(JournalPage(name='JOURNAL_LOG'))
        screen_manager.add_widget(FormJournalPage(name='FORM_JOURNAL'))  
        screen_manager.add_widget(FormBucketPage(name='FORM_BUCKET'))  
        screen_manager.add_widget(BucketListPage(name='BUCKET_LIST'))
        
        # Menambahkan StatisticPage dengan db_controller
        screen_manager.add_widget(StatisticPage(name='STATISTIC', db_controller=db_controller))
        
        # Menambahkan DatabasePage dengan db_entity
        screen_manager.add_widget(DatabasePage(name='LOCATION', db_entity=db_entity))

        # Add white background to the screen manager
        with screen_manager.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=screen_manager.size, pos=screen_manager.pos)

        # Bind size and position to update background accordingly
        screen_manager.bind(size=self._update_bg, pos=self._update_bg)

        # Sidebar for navigation
        sidebar = Sidebar(screen_manager=screen_manager)

        # Add sidebar and screen manager to the root layout
        root.add_widget(sidebar)
        root.add_widget(screen_manager)

        return root

    def _update_bg(self, instance, *args):
        """Update the background size and position of the ScreenManager."""
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

if __name__ == '__main__':
    MainApp().run()
