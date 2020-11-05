from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.icon_definitions import md_icons
from src.bcknd import Loader
from kivy.uix.widget import Widget



class MyLoader(Widget):
    url = 'https://moodup.team/test/info.php'
    loader = Loader(url)

    def show_recipe(self):
        self.recipe.text = str(self.loader.site_data['description'])


class MenuScreen(Screen):
    pass


class RecipeScreen(Screen):
    pass


class MoodApp(MDApp):
    data = {
        'mdi-virus-outline': 'Get the recipe',
        'mdi-facebook': 'Zaloguj przez Facebooka',
    }

    def __init__(self, **kwargs):
        self.title = "MoodApp"
        self.theme_cls.primary_palette = "Red"
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_file('main.kv')
        return screen


MoodApp().run()




''' 
do_scroll_y: True
            BoxLayout:
                size_hint_y: None
                orientation: 'vertical'
                height: self.minimum_height
                pos_hint: {'top': 0.9}

                Label:
                    text: 'wonderfull life!\n' * 100
                    color: (0,0,0,1)
                    size: self.texture_size
'''