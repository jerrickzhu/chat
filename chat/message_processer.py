from better_profanity import profanity

class MessageProcessor:
  """
    Process any messages. Currently supports cleaning messages from profanity
  """

  @staticmethod
  def clean_messages(message: str) -> str:
    cleaning_message: str = profanity.censor(message)
    return cleaning_message

