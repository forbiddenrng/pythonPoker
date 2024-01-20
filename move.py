def getPlayersResponse(message):
  while True:
    try:
      x=input(message)
      liczba=int(x)
      return liczba
    except ValueError:
      print("Wprowadź poprawną wartość!!!")