import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout # Import GridLayout design
from kivy.uix.button import Button # import buttons
from kivy.uix.label import Label # Import the simbols and widgets

class MainWindow(Screen): # Window for choosing the type of game
    pass

class OptionsWindow(Screen): # window for showing the computer dificulty levels
    pass


#class GameLayout(GridLayout): # Create the class with the design
#        def __init__(self, **kwargs): # handle as many kwargs as come
#            super(GameLayout, self).__init__(**kwargs)
#            
#            for i in range(0, (3 + 3)):
#                self.add_widget(Button(text = "Hello " + str(i)))
            

class GameWindow(Screen): # game window (where the game occurs)
    pass

class WindowManager(ScreenManager): # Transition between the windows
    pass

kv = Builder.load_file("my.kv") # Now the name of the kv file does not need to mathc the class name - App
sm = WindowManager()

screens = [MainWindow(name="main"), OptionsWindow(name="options"),GameWindow(name="game")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyApp(App):
    def build(self):
        self.title = 'Tic Tac Toe'
        return sm

if __name__ == "__main__":
    MyApp().run()