import socket

class Socket():
  def __init__(self) -> None:
    self.host_address: str = input("Enter the host address: ")
    self.port_to_connect: int = int(input("Enter the port: "))

  def connect_to_server(self) -> None:
    try:
      client_socket: socket = socket.socket
      client_socket.connect((self.host_address, self.port_to_connect))
    except Exception as e:
      print(f"Client failed to connect: {e}")


  
