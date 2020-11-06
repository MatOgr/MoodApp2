import os
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from src.bcknd import Loader
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivyauth.facebook_auth import initialize_fb, login_facebook, logout_facebook
from kivyauth.providers import login_providers


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
    current_provider = ''

    def __init__(self, **kwargs):
        self.title = "MoodApp"
        self.theme_cls.primary_palette = "Red"
        super().__init__(**kwargs)

    def build(self):
        initialize_fb(self.after_login, self.cancel_listener, self.error_listener)
        screen = Builder.load_file('main.kv')
        return screen

    def go_main(self):
        self.root.current = 'menu'
        self.root.transition.direction = 'right'

    def show_popup(self, nr):
        show = P()
        P.id = nr
        popupWindow = Popup(title='Zapisywanie obrazu %d' % nr,
                            content=show,
                            size_hint=(0.6, 0.4))
        popupWindow.open()

    def call(self, instance):
        if instance.icon == 'campfire':
            self.root.current = 'second'
            instance.parent.close_stack()
            self.root.transition.direction = 'left'
        elif instance.icon == 'facebook':
            self.fb_login()

    # secret departament
    def fb_login(self, *args):
        login_facebook()
        self.current_provider = login_providers.facebook

    def after_login(self, name, email, photo_uri):
        self.root.current = 'homescreen'
        self.update_ui(name, email, photo_uri)

    def after_logout(self):
        self.update_ui('', '', '')
        self.root.current = 'loginscreen'

    def update_ui(self, name, email, photo_uri):
        print("Welcome, {}".format(name))
        print("Your Email: {}".format(email) if email else "Your Email: Could not fetch email")

    def logout_(self):
        # logout(current_provider, self.after_logout)
        logout_facebook(self.after_logout)

    def cancel_listener(self):
        print("Login cancelled")

    def error_listener(self):
        print("Error logging in.")



MoodApp().run()