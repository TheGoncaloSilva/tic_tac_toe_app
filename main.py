from typing import Text
import random
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout # Import GridLayout design
from kivy.uix.button import Button # import buttons
from kivy.uix.label import Label # Import the simbols and widgets
from kivy.uix.popup import Popup # Import Popups
from kivy.uix.boxlayout import BoxLayout # Box layout for Popup

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

    game_mode = [] # mode wich the game is supposed to be played
    player1 = "X" # Player 1 always exists
    player2 = "O" # Player 2 is a bot in single player mode and another player in multiplayer
    active_player = 2 # Currently active player

    def build(self):
        self.title = 'Tic Tac Toe'
        return sm

    def load_multiplayer(self, asset): # update the game_mode to multiplayer
        self.game_mode = ['multiplayer', '']
    
    def load_solo_mode(self, difficulty): # update the game mode to single player and also it's difficulty
        self.game_mode = ['solo', difficulty]

    def choose_pos(self, asset): # when a player pressed a button
        if asset.text == "" and (self.player1 != "" and self.player2 != ""):
            if self.active_player % 2 == 0:
                asset.text = self.player1
            else: 
                asset.text = self.player2   
        else: # If the conditions aren't met, it will give a warning to the user
            self.popup_manager(False, 'OOPS! :(', 'An Error occurred trying to register your position. Please reset the game or try again later')
    
    def choose_player(self): # Choose the player to start the game
        self.active_player = random.randrange(0, 2)


    def clear_table(self): # Reset the game
        self.root.ids.gbtn_1.text = ""
        self.root.ids.gbtn_2.text = ""
        self.root.ids.gbtn_3.text = ""
        self.root.ids.gbtn_4.text = ""
        self.root.ids.gbtn_5.text = ""
        self.root.ids.gbtn_6.text = ""
        self.root.ids.gbtn_7.text = ""
        self.root.ids.gbtn_8.text = ""
        self.root.ids.gbtn_9.text = ""
        self.choose_player()

    def analyze_moves():
        pass

    def game_ended():
        pass

    # Flexible way of showing Popups, parameters:
    #   - self...
    #   - status of the message -> True or False and act accordingly
    #   - Title given to the Popup
    #   - The Message itself
    def popup_manager(self, status, title, message):
        if status: # Good Popup
            boxl = BoxLayout(orientation="vertical")
            boxl2 =BoxLayout(orientation="horizontal", size_hint_y=None, height=40)
            pop = Popup(title=title, content=boxl, size_hint=(0.75,0.8))
            document = Label(text=message,markup=True, valign='top')
            button = Button(text='Dismiss', size_hint_y=None, height=40)
            button2 = Button(text="Do Something", size_hint_y=None, height=40)
            button.bind(on_press=(lambda x:pop.dismiss()))
            boxl.add_widget(document)
            boxl2.add_widget(button)
            boxl2.add_widget(button2)
            boxl.add_widget(boxl2)
            document.bind(size=document.setter('text_size'))

        else: # Bad Popup
            boxl = BoxLayout(orientation="vertical")
            boxl2 =BoxLayout(orientation="horizontal", size_hint_y=None, height=40)
            pop = Popup(title=title, content=boxl, size_hint=(0.75,0.8))
            document = Label(text=message,markup=True, valign='top')
            button = Button(text='Dismiss', size_hint_y=None, height=40)
            button2 = Button(text="Reset Game", size_hint_y=None, height=40)
            button.bind(on_press=(lambda x:pop.dismiss()))
            boxl.add_widget(document)
            boxl2.add_widget(button)
            boxl2.add_widget(button2)
            boxl.add_widget(boxl2)
            document.bind(size=document.setter('text_size'))
        pop.open() # Open the Popup

    


if __name__ == "__main__":
    MyApp().run()