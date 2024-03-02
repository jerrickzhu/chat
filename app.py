from kivy.app import App
from client import Client
from main_gui import MainGUI

class MyApp(App):
  def build(self):
    client = Client("0.0.0.0", 5001)
    return MainGUI(client)

if __name__ == '__main__':
  MyApp().run()