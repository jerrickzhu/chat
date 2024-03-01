# client_manager_instance is a global instance that keeps track of clients in a list.
from client_manager import client_manager_instance as CLIENT_MANAGER
from typing import List
# Import MessageHandler to clean messages from profanity.
from message_processer import MessageProcessor
import socket

class ClientHandler:
  """
    Manage individual client connections to server. 
    Handles tasks like accepting client connections,
    manage client communications, and broadcasting messages.
  """

  def handle_client(self, client_socket: socket.socket) -> None:
    """
      Handles communication from a client. Receives the message data
      and processes it, followed by broadcasting it.
    """
    CLIENT_MANAGER.add_client(client_socket)

    while True:
      try:
        message: str = client_socket.recv(1024).decode()
        if not message:
          break
        clean_message: str = MessageProcessor.clean_messages(message)
        print(f"Message received: {clean_message}")

        # Broadcast message to all other clients
        self.broadcast_message(clean_message)
      except (ConnectionAbortedError, ConnectionRefusedError):
        CLIENT_MANAGER.remove_client(client_socket)
        client_socket.close()
        print(f"A client disconnected.")


  def broadcast_message(self, message: str) -> None: 
    client_list: List[socket.socket] = CLIENT_MANAGER.get_clients()
    for client in client_list:
      try:
        client.send(message.encode())
      except Exception as e:
        print(f"Could not send this message. See error: {e}")
