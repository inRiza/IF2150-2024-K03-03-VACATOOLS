from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.graphics import Color, Rectangle
from src.components.sidebar import Sidebar
from src.boundary.homePage import HomePage
from src.boundary.journalPage import JournalPage
from src.boundary.bucketListPage import BucketListPage
from src.boundary.page3 import Page3
from src.boundary.page4 import Page4
from src.boundary.formJournalPage import FormJournalPage  # Import FormJournalPage
from src.boundary.formBucketPage import FormBucketPage  # Import FormJournalPage

class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')

        # Screen manager to handle navigation
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomePage(name='HOME'))
        screen_manager.add_widget(JournalPage(name='JOURNAL_LOG'))
        screen_manager.add_widget(FormJournalPage(name='FORM_JOURNAL'))  
        screen_manager.add_widget(FormBucketPage(name='FORM_BUCKET'))  
        screen_manager.add_widget(BucketListPage(name='BUCKET_LIST'))
        screen_manager.add_widget(Page3(name='STATISTIC'))
        screen_manager.add_widget(Page4(name='LOCATION'))

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
