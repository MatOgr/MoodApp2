import kivy
from kivy.app import App
from kivy.uix.label import Label


class MoodApp(kivy.app.App):
    def build(self):
        return Label(text='Ta jes')




if __name__ == '__main__':
    MoodApp().run()
