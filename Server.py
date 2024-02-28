import socket

class Server():
  def __init__(self) -> None:
    self.host_address: str = "0.0.0.0"
    self.PORT: int = 5000
    self.server_socket: socket = None
    self.number_of_listens: int = int(input("Please enter the number of people the server can listen to at a time: "))

