import socket
from threading import Thread


class Client:
  def __init__(self) -> None:
    self.host_address: str = input("Enter the host address: ")
    self.port_to_connect: int = int(input("Enter the port: "))
    self.client_socket: socket.socket = None
    # Variable to determine if the client is connected or not.
    self.CONNECTED = False


  def connect_to_server(self) -> None:
    try:
      self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

    except Exception as e:
      print(f"Failed to receive message: {e}")
    
  def start_client(self) -> None:
    self.connect_to_server()

    receive_thread: Thread = Thread(target=self.receive_messages)
    receive_thread.start()

    while self.CONNECTED:
        message = input()
        self.send_message(message)

if __name__ == "__main__":
    client: Client = Client()
    client.start_client()
  


  
