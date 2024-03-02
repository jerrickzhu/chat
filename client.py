import socket
from threading import Thread


class Client:
  def __init__(self, host_address: str, port: int) -> None:
    self.host_address: str = host_address
    self.port_to_connect: int = port
    self.client_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Variable to determine if the client is connected or not.
    self.CONNECTED: bool = False
    self.message_received: str = ""

  def connect_to_server(self) -> None:
    try:
      self.client_socket.connect((self.host_address, self.port_to_connect))
      self.CONNECTED = True
      print("You have successfully connected to the server!")
    except Exception as e:
      print(f"Client failed to connect: {e}")

  def send_message(self, message: str) -> None:
    try:
      self.client_socket.send(message.encode())
    except Exception as e:
      print(f"Failed to send message: {e}")

  def receive_messages(self) -> None:
    try:
      while True:
        message_data = self.client_socket.recv(1024).decode()
        print(message_data)
        if not message_data:
          break
        self.message_received = message_data
    except Exception as e:
      print(f"Failed to receive message: {e}")

  def get_message(self) -> str:
    message_to_send: str = self.message_received
    self.message_received = ""
    return message_to_send
    
  def start_client(self) -> None:
    try:
      self.connect_to_server()

      receive_thread: Thread = Thread(target=self.receive_messages)
      receive_thread.start()

      while self.CONNECTED:
          message = input()
          self.send_message(message)
    except Exception as e:
      self.CONNECTED = False
      print(f"Client start failed! {e}")



  
