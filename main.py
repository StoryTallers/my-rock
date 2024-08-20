# LIBRARY
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

# ADITIONAL FILE
from mainScreen import sc

# INSTANCE

class MainPage(Screen):
    pass

class GymPage(Screen):
    pass

class TrenerPage(Screen):
    pass

class ProfilPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class mainApp(App):
    def build(self):
        return kv

kv = Builder.load_file('Window.kv')


# main process run
if __name__ == "__main__":
    mainApp().run()