import kivy
from kivy.app import App
from kivy.uix.label import Label # Import the simbols and widgets
import os
#os.environ["SDL_VIDEODRIVER"] = "x11"

class MyApp(App):
    def build(self): # Construir o UI
        return Label(text = "Hello World")

if __name__ == "__main__":
    MyApp().run()