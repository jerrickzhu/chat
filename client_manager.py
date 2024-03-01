import socket
from typing import List

class ClientManager():
  """
    Manages clients in a list and offers operations to add, remove, and checkout
    list of clients.
  """
  _instance = None

  def __new__(cls):
    if not cls._instance:
      cls._instance = super().__new__(cls)
      cls._instance.clients = []
    return cls._instance

  def add_client(self, client: socket.socket) -> None:
    try:
      self.clients.append(client)
      print("Successfully added a new client")
    except Exception as e:
      print(f"Failed to add a new client to client tracking list. {e}")

  def remove_client(self, client: socket.socket) -> None:
    try:
      self.clients.remove(client)
      print("Removed client")
    except Exception as e:
      print(f"Failed to remove client from the list {e}")

  def get_clients(self) -> List[socket.socket]:
    return self.clients

client_manager_instance: ClientManager = ClientManager()