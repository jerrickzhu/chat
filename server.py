import socket

class Server():
  def __init__(self) -> None:
    self.host_address: str = "0.0.0.0"
    self.PORT: int = 5001
    self.server_socket: socket = None
    self.conn: socket = None
    self.number_of_listens: int = int(input("Please enter the number of people the server can listen to at a time: "))

  def initialize_socket(self) -> None:
    """
      Initializes the socket with the host address and port.
    """
    try:
      self.server_socket = socket.socket()
      self.server_socket.bind((self.host_address, self.PORT))
      print("The socket instance has successfully been instantiated.")
    except Exception as e:
      print(f"Initializing a socket instance has failed: {e}")

  def accept_client_connections(self) -> None:
    try:
      self.server_socket.listen(self.number_of_listens)
      self.conn, address = self.server_socket.accept()
      print(f"We have a new client from {address}")
    except Exception as e:
      print(f"Failed to accept the client connection here: {e}")

