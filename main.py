from client_manager import ClientManager
from server import Server

def main():
  client_manager: ClientManager = ClientManager()
  server: Server = Server()

  server.start_server()

if __name__ == "__main__":
  main()