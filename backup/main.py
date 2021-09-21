import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout # Import GridLayout design
from kivy.uix.button import Button # import buttons
from kivy.uix.label import Label # Import the simbols and widgets

class MainWindow(Screen): # Window for choosing the type of game
    pass

class OptionsWindow(Screen): # window for showing the computer dificulty levels
    pass

def Generate_Grid(rows, columns, self):
    # First Layout
    #self.cols = 1
    #self.size_hint = None, None
    #app = App.get_running_app # get the current running app
    
    #self.size = app.root.width - 10, app.root.height - 130 # 65 each part at the top
    #self.pos = 5, 65

    # Second Layout
    self.inside = GridLayout()
    #self.inside.cols = columns
    #self.inside.rows = rows
    #self.inside.size_hint = None, None
    #self.inside.size = app.root.width - 10, app.root.height - 130 # 65 each part at the top
    #self.inside.pos = 5, 65

    for i in range(0, (rows + columns)):
        self.inside.add_widget(Button(text = "Hello " + str(i)))


class GameLayout(GridLayout): # Create the class with the design
        def __init__(self, **kwargs): # handle as many kwargs as come
            super(GameLayout, self).__init__(**kwargs)
            Generate_Grid(3, 3, self) # Use our function to create a 'table' GridLayout
            

            game_window = GameWindow()
            game_layout = GameLayout()
            game_window.add_widget(game_layout)

class GameWindow(Screen): # game window (where the game occurs)
    Generate_Grid(3, 3, GridLayout)
    pass

class WindowManager(ScreenManager): # Transition between the windows
    pass

kv = Builder.load_file("my.kv") # Now the name of the kv file does not need to mathc the class name - App
sm = WindowManager()

screens = [MainWindow(name="main"), OptionsWindow(name="options"),GameWindow(name="game")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        self.title = 'Tic Tac Toe'
        return sm

if __name__ == "__main__":
    MyMainApp().run()