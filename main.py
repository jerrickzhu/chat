from chat.client_manager import ClientManager
from threading import Thread

from server import Server
from client import Client

def main():
  client_manager: ClientManager = ClientManager()
  server: Server = Server()

  
  server_thread: Thread = Thread(target=server.start_server)
  server_thread.start()

if __name__ == "__main__":
  main()