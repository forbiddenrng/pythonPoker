import os
SMALLBLIND = 10
currentBet= 0
pot=0

def placeABet(PLAYERSARRAY,player, bet):
  PLAYERSARRAY[player]['credits']-=bet
  global pot
  global currentBet
  pot+=bet
  currentBet=bet


def setNextPlayer(currentPlayer, arrLen):
  if currentPlayer == arrLen-1:
    return 0
  else:
    currentPlayer+=1
    return currentPlayer

def displayPlayers(PLAYERSARRAY):
  for player in PLAYERSARRAY:
    print(f"{player['nick']} {player['role']}: {player['credits']}$")
  print(f"W puli aktualnie jest: {pot}$")
  print(f"Wysokość ostatniego zakładu: {currentBet}$")


def makeMove(PLAYERSARRAY, playerOnMove, moves):
  print(f"Ruch gracza: {PLAYERSARRAY[playerOnMove]['nick']}")
  i=1
  for move in moves:
    print(f"{i}. {move}")
    i+=1
  playersMove=""
  while not (playersMove==1 or playersMove==2 or playersMove==3):
    playersMove = int(input("Twój wybór: "))
    if not (playersMove==1 or playersMove==2 or playersMove==3):
      print("Wybierz poprawną opcję")
  ## czyszczenie ekranu i wyświetlenie graczy
  os.system('cls')
  displayPlayers(PLAYERSARRAY)
  return moves[playersMove-1]

def fold(PLAYERSARRAY, playerIndex):
  popPlayer = PLAYERSARRAY.pop(playerIndex)
  return PLAYERSARRAY

def call(PLAYERSARRAY, playerOnMove):
  placeABet(PLAYERSARRAY, playerOnMove, currentBet)
  nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))


def continueBidding(PLAYERSARRAY, playerOnMove, possibleMoves):
  decision=makeMove(PLAYERSARRAY, playerOnMove, possibleMoves)
  if decision=="fold":
    newPlayersArray = fold(PLAYERSARRAY, playerOnMove)
    if len(newPlayersArray)==1:
      print(f"Wygrywa gracz {newPlayersArray[0]['nick']}")
      return 0
    nextPlayer = setNextPlayer(playerOnMove-1, len(newPlayersArray))
    continueBidding(newPlayersArray, nextPlayer, ['fold', 'call', 'raise'])
  elif decision=="call":
    placeABet(PLAYERSARRAY, playerOnMove, currentBet)
    nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'])
  elif decision=="raise":
    bet=0
    while True:
      bet=int(input("Podaj wartość bet'a: "))
      if bet>PLAYERSARRAY[playerOnMove]['credits']:
        print("Nie masz tyle na koncie!!! Podaj mniejszy zakład")
      elif bet<currentBet:
        print("Zakład nie może być mniejszy niż poprezdni!")
      else:
        break 

    placeABet(PLAYERSARRAY, playerOnMove, bet)
    nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'])


def startBidding(oryginalArray):
  PLAYERSARRAY = oryginalArray.copy()
  playerOnMove=0
  for i in range(len(PLAYERSARRAY)):
    if PLAYERSARRAY[i]['role']=='SB':
      playerOnMove=i
      break
  
  placeABet(PLAYERSARRAY, playerOnMove, SMALLBLIND) ## small blind
  playerOnMove = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
  placeABet(PLAYERSARRAY, playerOnMove, 2*SMALLBLIND) ## big blind
  playerOnMove = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
  displayPlayers(PLAYERSARRAY)
  continueBidding(PLAYERSARRAY,playerOnMove, ['fold', 'call', 'raise'])
  




