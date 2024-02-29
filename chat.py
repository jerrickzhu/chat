class Chat():
  """
    Chat class to handle all chat functions.
  """
  @staticmethod
  def show_messages(clients, message: str) -> None:
    """ Shows messages to all clients. """
    try:
      for client in clients:
        client.send(message)
    except Exception as e:
      print(f"Could not send messages: {e}")