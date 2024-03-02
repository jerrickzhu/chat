from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import threading

class ChatGUI(BoxLayout):
  def __init__(self, client, **kwargs):
    super().__init__(**kwargs)
    self.client = client
    self.orientation = 'vertical'

    self.chat_display = TextInput(readonly=True, multiline=True)
    self.add_widget(self.chat_display)

    self.message_input = TextInput(multiline=False)
    self.add_widget(self.message_input)

    send_button = Button(text='Send')
    send_button.bind(on_press=self.send_message)
    self.add_widget(send_button)

    # Start thread for client connection and receiving
    threading.Thread(target=self.client.start_client).start()

    # Check for incoming messages periodically
    Clock.schedule_interval(self.receive_messages, 1.0)

  def send_message(self, instance) -> None:
    message = self.message_input.text.strip()
    if message:
        # Start thread for sending messages 
        threading.Thread(target=self.client.send_message, args=(message,)).start()
        self.message_input.text = ''

  def receive_messages(self, dt) -> None:
    message: str = self.client.get_message()
    if message:
        self.chat_display.text += f'\n{message}'
  
     
