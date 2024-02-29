from typing import List
from threading import Thread
from better_profanity import profanity
import socket

class Server():
  """
    This class defines the set up the server, including any listening
    and client connections that may happen.
  """
  def __init__(self) -> None:
    self.host_address: str = "0.0.0.0"
    self.PORT: int = 5001
    self.server_socket: socket = None
    self.clients: List[socket.socket] = None

  def initialize_socket(self) -> None:
    """ Initializes the socket with the host address and port. """
    try:
      self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.server_socket.bind((self.host_address, self.PORT))
      print("The socket instance has successfully been instantiated.")
    except Exception as e:
      print(f"Initializing a socket instance has failed: {e}")

  def accept_client_connections(self) -> None:
    """ Connects client to server. """
    try:
      while True:
        self.server_socket.listen()
        client, client_address = self.server_socket.accept()
        print(f"We have a new client from {client_address}")
        self.clients.append(client)
        client_thread: Thread = Thread(target=MessageHandler.handle_messages, args=(self, client,))
        client_thread.start()

    except Exception as e:
      print(f"Failed to accept the client connection here: {e}")

  def start_server(self) -> None:
    try:
      self.initialize_socket()
      self.accept_client_connections()
    except Exception as e:
      print(f"Failed starting server: {e}")



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

class Chat():
  """
    Chat class to handle all chat functions.
  """
  @staticmethod
  def show_messages(clients, message: str) -> None:
    """ Shows messages to all clients. """
    try:
      for client in clients:
        client.send(message)
    except Exception as e:
      print(f"Could not send messages: {e}")