from kivy.uix.boxlayout import BoxLayout
from drawing_gui import DrawingWidget
from chat_gui import ChatGUI

class MainGUI(BoxLayout):
  def __init__(self, client, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'horizontal'

    drawing_widget = DrawingWidget()
    chat_gui = ChatGUI(client)

    self.add_widget(drawing_widget)
    self.add_widget(chat_gui)
