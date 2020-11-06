import os

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from src.bcknd import Loader
from kivy.uix.widget import Widget
from kivy.utils import platform


class MyLoader(Widget):
    url = 'https://moodup.team/test/info.php'
    loader = Loader(url)
    if platform == 'android':
        loader.SAVE_FOLDER = os.getenv('DIRECTORY_PICTURES')

    def show_recipe(self):
        self.recipe.text = str(self.loader.site_data['description'])


class MenuScreen(Screen):
    pass


class RecipeScreen(Screen):
    pass


class P(FloatLayout):
    id = 0


class MoodApp(MDApp):
    url = 'https://moodup.team/test/info.php'
    loader = Loader(url)
    if platform == 'android':
        loader.SAVE_FOLDER = os.getenv('DIRECTORY_PICTURES')
    data = {
        'campfire': 'Get the recipe',
        'facebook': 'Zaloguj przez Facebooka'}

    def __init__(self, **kwargs):
        self.title = "MoodApp"
        self.theme_cls.primary_palette = "Red"
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_file('main.kv')
        return screen

    def go_main(self):
        self.root.current = 'menu'
        self.root.transition.direction = 'right'

    def show_popup(self, nr):
        show = P()
        P.id = nr
        popup_window = Popup(title='Zapisywanie obrazu %d' % nr,
                             content=show,
                             size_hint=(0.6, 0.4))
        popup_window.open()

    def call(self, instance):
        if instance.icon == 'campfire':
            self.root.current = 'second'
            instance.parent.close_stack()
            self.root.transition.direction = 'left'


MoodApp().run()
