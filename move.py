import os
def getPlayersResponse(message):
  while True:
    try:
      x=input(message)
      liczba=int(x)
      return liczba
    except ValueError:
      print("Wprowadź poprawną wartość!!!")


def makeMove(PLAYERSARRAY, playerOnMove, moves):
  
  print(f"Ruch gracza: {PLAYERSARRAY[playerOnMove]['nick']}")
  i=1
  for move in moves:
    print(f"{i}. {move}")
    i+=1
  playersMove=0
  while not (playersMove==1 or playersMove==2 or playersMove==3):
    playersMove = getPlayersResponse("Twój wybór: ")
    if playersMove==1 or playersMove==2 or playersMove==3:
      break
  ## czyszczenie ekranu i wyświetlenie graczy
  os.system('cls')
  #displayPlayers(PLAYERSARRAY)
  return moves[playersMove-1]

def getPrevPlayer(PLAYERSARRAY, playerOnMove):
  if playerOnMove==0:
    return len(PLAYERSARRAY)-1
  else:
    return playerOnMove-1
def setNextPlayer(currentPlayer, arrLen):
  if currentPlayer == arrLen-1:
    return 0
  else:
    currentPlayer+=1
    return currentPlayer