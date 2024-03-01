from threading import Thread
from client_handler import ClientHandler
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
    self.CLIENT_HANDLER: ClientHandler = ClientHandler()

  def initialize_socket(self) -> None:
    """ Initializes the socket with the host address and port. """
    try:
      self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.server_socket.bind((self.host_address, self.PORT))
      print("The socket instance has successfully been instantiated.")
      self.accept_client_connections()
    except Exception as e:
      print(f"Initializing a socket instance has failed: {e}")

  def accept_client_connections(self) -> None:
    """ Connects client to server. """
    client: socket.socket = None
    try:
      self.server_socket.listen()
      while True:
        client, client_address = self.server_socket.accept()
        print(f"We have a new client from {client_address}")

        # Starts a thread for the client. Each client will have the client handler
        # handle all messages received.
        client_thread: Thread = Thread(target=self.CLIENT_HANDLER.handle_client, args=(client,))
        client_thread.start()
    except (ConnectionAbortedError, ConnectionRefusedError):
      print(f"User disconnected")

  def start_server(self) -> None:
    """ Start server with this method. """
    try:
      self.initialize_socket()
    except Exception as e:
      print(f"Failed starting server: {e}")


