import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen): # Window for choosing the type of game
    pass

class OptionsWindow(Screen): # window for showing the computer dificulty levels
    pass

class GameWindow(Screen): # game window (where the game occurs)
    pass

class WindowManager(ScreenManager): # Transition between the windows
    pass

kv = Builder.load_file("my.kv") # Now the name of the kv file does not need to mathc the class name - App

class MyMainApp(App):
    def build(self):
        self.title = 'Tic Tac Toe'
        return kv

if __name__ == "__main__":
    MyMainApp().run()