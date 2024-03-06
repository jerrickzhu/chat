import socket
from typing import List

class ClientManager:
  _instance = None

  def __new__(cls):
    if not cls._instance:
      cls._instance = super().__new__(cls)
      cls._instance.drawing_clients = []
      cls._instance.chat_clients = []
    return cls._instance

  def add_drawing_client(self, client: socket.socket) -> None:
    try:
      if client not in self.drawing_clients:
        self.drawing_clients.append(client)
        print("Successfully added a new drawing client")
    except Exception as e:
      print(f"Failed to add a new drawing client: {e}")

  def remove_drawing_client(self, client: socket.socket) -> None:
    try:
      if client in self.drawing_clients:
          self.drawing_clients.remove(client)
          print("Removed drawing client")
    except Exception as e:
      print(f"Failed to remove drawing client: {e}")

  def get_drawing_clients(self) -> List[socket.socket]:
    return self.drawing_clients

  def add_chat_client(self, client: socket.socket) -> None:
    try:
      if client not in self.chat_clients:
        self.chat_clients.append(client)
        print("Successfully added a new chat client")
    except Exception as e:
      print(f"Failed to add a new chat client: {e}")

  def remove_chat_client(self, client: socket.socket) -> None:
    try:
      if client in self.chat_clients:
        self.chat_clients.remove(client)
        print("Removed chat client")
    except Exception as e:
      print(f"Failed to remove chat client: {e}")

  def get_chat_clients(self) -> List[socket.socket]:
    return self.chat_clients

client_manager_instance: ClientManager = ClientManager()
