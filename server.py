from typing import List
from threading import Thread
from client_manager import client_manager_instance
from message_handler import MessageHandler

import socket
import json

class Server():
  """
    This class defines the set up the server, including any listening
    and client connections that may happen.
  """
  def __init__(self) -> None:
    self.host_address: str = "0.0.0.0"
    self.PORT: int = 5001
    self.server_socket: socket = None
    self.CLIENT_MANAGER = client_manager_instance

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
    client: socket.socket = None
    try:
      while True:
        self.server_socket.listen()
        client, client_address = self.server_socket.accept()
        print(f"We have a new client from {client_address}")
        self.CLIENT_MANAGER.add_client(client)
        client_thread: Thread = Thread(target=MessageHandler.handle_messages, args=(client,))
        client_thread.start()
    except (ConnectionAbortedError, ConnectionRefusedError):
      self.CLIENT_MANAGER.remove_client(client)
      client.close()
      print(f"User disconnected")

  def start_server(self) -> None:
    try:
      self.initialize_socket()
      self.accept_client_connections()
    except Exception as e:
      print(f"Failed starting server: {e}")


