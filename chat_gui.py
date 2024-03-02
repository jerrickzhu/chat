from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from client import Client
import threading

class ChatGUI(App):
  def __init__(self, client, **kwargs):
    super().__init__(**kwargs)
    self.client = client
    self.message_input = None
    self.chat_display = None

  def build(self):
    layout = BoxLayout(orientation='vertical')

    self.chat_display = TextInput(readonly=True, multiline=True)
    layout.add_widget(self.chat_display)

    self.message_input = TextInput(multiline=False)
    layout.add_widget(self.message_input)

    send_button = Button(text='Send')
    send_button.bind(on_press=self.send_message)
    layout.add_widget(send_button)

    threading.Thread(target=self.client.start_client).start()

    # Check for incoming messages periodically
    Clock.schedule_interval(self.receive_messages, 1.0)

    return layout

  def send_message(self, instance) -> None:
    message = self.message_input.text.strip()
    if message:
        threading.Thread(target=self.client.send_message, args=(message,)).start()
        self.message_input.text = ''

  def receive_messages(self, dt) -> None:
    message: str = self.client.get_message()
    if message:
        self.chat_display.text += f'\n{message}'

if __name__ == '__main__':

  client = Client("0.0.0.0", 5001)
  
  ChatGUI(client).run()