import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from src.bcknd import Loader
from kivy.config import Config
from kivy.uix.image import AsyncImage

Config.set('graphics', 'resizable', True)


class MyLoader(Widget):
    url = 'https://moodup.team/test/info.php'
    loader = Loader(url)
    # title = ObjectProperty(loader.get_data_content('title'))
    # recipe = ObjectProperty(loader.get_data_content('description'))
    # ingredients = ObjectProperty(loader.get_data_content('ingredients'))
    # preparing = ObjectProperty(loader.get_data_content('preparing'))

    def show_recipe(self):
        self.recipe.text = str(self.loader.site_data['description'])


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("mood.kv")


class MoodApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MoodApp().run()
