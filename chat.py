import socket
from server import Server

class Chat():

  @staticmethod
  def handle_messages(server: Server, client: socket.socket):
    """ Handles messages across all clients. 
      Parameters:
        client - socket object that is an instance of a client
    """
    try:
      while True:
        message: bytes = client.recv(1024).decode()
        if not message or not isinstance(message, bytes):
          break
        Chat.show_messages(message.encode())
    except (ConnectionAbortedError, ConnectionResetError):
      server.clients.remove(client)
      print(f"A client has disconnected")
      client.close()

  @staticmethod
  def show_messages(clients, message: str) -> None:
    """ Shows messages to all clients. """
    try:
      for client in clients:
        client.send(message)
    except Exception as e:
      print(f"Could not send messages: {e}")