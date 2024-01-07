SMALLBLIND = 10
def placeABet(PLAYERSARRAY,player, bet):
  PLAYERSARRAY[player]['credits']-=bet


def setNextPlayer(currentPlayer, arrLen):
  if currentPlayer == arrLen-1:
    return 0
  else:
    currentPlayer+=1
    return currentPlayer

def displayPlayers(PLAYERSARRAY):
  for player in PLAYERSARRAY:
    print(f"{player['nick']} {player['role']}: {player['credits']}$")

def makeMove(PLAYERSARRAY, playerOnMove, moves):
  print(f"Ruch gracza: {PLAYERSARRAY[playerOnMove]['nick']}")
  i=1
  for move in moves:
    print(f"{move}")
    i+=1
  playersMove = int(input("Twój wybór: "))



def startBidding(PLAYERSARRAY):
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
  




