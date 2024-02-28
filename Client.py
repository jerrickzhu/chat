import socket

class Socket():
  def __init__(self) -> None:
    self.host_address: str = input("Enter the host address: ")
    self.port_to_connect: int = int(input("Enter the port: "))
  
