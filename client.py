import socket
from threading import Thread
from message_handler import MessageHandler


class Client():
  def __init__(self) -> None:
    self.host_address: str = input("Enter the host address: ")
    self.port_to_connect: int = int(input("Enter the port: "))
    self.client_socket: socket.socket = None


  def connect_to_server(self) -> None:
    try:
      self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.client_socket.connect((self.host_address, self.port_to_connect))

    except Exception as e:
      print(f"Client failed to connect: {e}")

  def send_message(self, message: str) -> None:
    try:
      self.client_socket.send(message.encode())
    except Exception as e:
      print(f"Failed to send message: {e}")

if __name__ == "__main__":
    new_client: Client = Client()
    new_client.connect_to_server()

    while True:
        message = input("Enter message: ")
        new_client.send_message(message)
  


  
