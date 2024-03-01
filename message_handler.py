from chat import Chat
from better_profanity import profanity
from client_manager import client_manager_instance
import socket

class MessageHandler():

  @staticmethod
  def handle_messages(client: socket.socket):
    """ Handles messages across all clients. 
      Parameters:
        client - socket object that is an instance of a client
    """
    try:
      while True:
        message: str = client.recv(1024).decode()
        if not message or not isinstance(message, str):
          break
        print(message)
        clean_message_to_send: str = MessageHandler.clean_messages(message)
        Chat.show_messages(client_manager_instance.get_clients(), clean_message_to_send)
    except (ConnectionAbortedError, ConnectionResetError):
      print(f"A client has disconnected")
 

  @staticmethod
  def clean_messages(message: str) -> str:
    cleaning_message: str = profanity.censor(message)
    return cleaning_message

