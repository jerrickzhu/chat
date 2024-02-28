import socket

class Server():
  def __init__(self) -> None:
    self.host_address: str = "0.0.0.0"
    self.PORT: int = 5001
    self.server_socket: socket = None
    self.number_of_listens: int = int(input("Please enter the number of people the server can listen to at a time: "))

  def initialize_socket(self) -> None:
    try:
      self.server_socket = socket.socket()
      self.server_socket.bind((self.host_address, self.PORT))
      print("The socket instance has successfully been instantiated.")
    except Exception as e:
      print(f"Initializing a socket instance has failed: {e}")
