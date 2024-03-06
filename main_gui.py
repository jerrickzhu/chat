from kivy.uix.boxlayout import BoxLayout
from chat_gui import ChatGUI

class MainGUI(BoxLayout):
  def __init__(self, client, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'horizontal'

    chat_gui = ChatGUI(client)

    self.add_widget(chat_gui)
