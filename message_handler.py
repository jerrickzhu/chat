from chat import Chat
from better_profanity import profanity
import socket

class Server:
  pass

class MessageHandler():

  @staticmethod
  def handle_messages(server: Server, client: socket.socket):
    """ Handles messages across all clients. 
      Parameters:
        client - socket object that is an instance of a client
    """
    try:
      while True:
        message: str = client.recv(1024).decode()
        if not message or not isinstance(message, str):
          break
        clean_message_to_send: str = MessageHandler.clean_messages(message)
        Chat.show_messages(clean_message_to_send)
    except (ConnectionAbortedError, ConnectionResetError):
      server.clients.remove(client)
      print(f"A client has disconnected")
      client.close()

  @staticmethod
  def clean_messages(message: str) -> str:
    cleaning_message: str = profanity.censor(message)
    return cleaning_message

