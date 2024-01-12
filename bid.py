import os, cards
SMALLBLIND = 10
currentBet= 0
pot=0
MAXBID=200
checkNumber=0
playersBets={
  
}
def setPlayersBetsList(PLAYERSARRAY):
  for player in PLAYERSARRAY:
    playersBets[player['nick']]=[]
  
def getPrevPlayer(PLAYERSARRAY, playerOnMove):
  if playerOnMove==0:
    return len(PLAYERSARRAY)-1
  else:
    return playerOnMove-1

def getPlayersBetsSum(PLAYERSARRAY, player):
  nick=PLAYERSARRAY[player]['nick']
  playerBetsArray = playersBets.get(nick)
  if len(playerBetsArray)==0:
    return 0
  betsSum = sum(playerBetsArray)
  return betsSum


def placeABet(PLAYERSARRAY,player, bet):
  PLAYERSARRAY[player]['credits']-=bet
  global pot
  global currentBet
  pot+=bet
  if bet>currentBet:
    currentBet=bet
  ## dodanie beta do playersBets
  playersBets[PLAYERSARRAY[player]['nick']].append(bet)

def isBiddingEnd(PLAYERSARRAY):
  betsSum=[]
  for player in PLAYERSARRAY:
    playerNick=player['nick']
    playerBetsSum=0
    for bet in playersBets[playerNick]:
      playerBetsSum+=bet
    betsSum.append(playerBetsSum)
  firstValue=betsSum[0]
  for i in range(len(betsSum)):
    if betsSum[i] != firstValue:
      return False
  return True


def setNextPlayer(currentPlayer, arrLen):
  if currentPlayer == arrLen-1:
    return 0
  else:
    currentPlayer+=1
    return currentPlayer

def displayCards(cardsToDisplay):
  if not len(cardsToDisplay)==0:
    print("Karty na stole: ", end="")
    for card in cardsToDisplay:
      cardName=cards.getCardName(card['value'])
      print(f"{cardName} {card['color']}, ", end="")
    print()

def displayPlayers(PLAYERSARRAY, displayedCards=[]):
  for player in PLAYERSARRAY:
    print(f"{player['nick']} {player['role']}: {player['credits']}$")
  print(f"W puli aktualnie jest: {pot}$")
  print(f"Wysokość ostatniego zakładu: {currentBet}$")
  displayCards(displayedCards)


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
  #displayPlayers(PLAYERSARRAY)
  return moves[playersMove-1]

def fold(PLAYERSARRAY, playerIndex):
  popPlayer = PLAYERSARRAY.pop(playerIndex)
  return PLAYERSARRAY

def call(PLAYERSARRAY, playerOnMove):
  betToCall=0
  ### sprawdzenie ile ostatni gracz wrzucił łącznie do puli
  prevPlayer = getPrevPlayer(PLAYERSARRAY, playerOnMove)
  prevPlayerBetsSum= getPlayersBetsSum(PLAYERSARRAY, prevPlayer)
  currentPlayerBetsSum = getPlayersBetsSum(PLAYERSARRAY, playerOnMove)
  betToCall=prevPlayerBetsSum-currentPlayerBetsSum

  placeABet(PLAYERSARRAY, playerOnMove, betToCall)
  nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))

def getPlayersResponse(message):
  while True:
    try:
      x=input(message)
      liczba=int(x)
      return liczba
    except ValueError:
      print("Wprowadź poprawną wartość!!!")


def betMove(PLAYERSARRAY, playerOnMove):
  bet=0
  while bet>MAXBID or bet<=0 or bet>PLAYERSARRAY[playerOnMove]['credits']:
    bet = getPlayersResponse("Podaj wartość bet'a: ")
  os.system('cls')
  placeABet(PLAYERSARRAY, playerOnMove, bet)
  global currentBet
  currentBet=bet



def continueBidding(PLAYERSARRAY, playerOnMove, possibleMoves, biddingStart=False, displayedCards=[]):
  ## sprawdzenie czy licytacja się nie skończyła -- czy każdy gracz dał tyle samo do puli
  ## jeśli każdy dał tyle samo do puli to licytacja się kończy i przechodzi do następnego etapu.
  isEnd=isBiddingEnd(PLAYERSARRAY)
  if isEnd and not biddingStart:
    return PLAYERSARRAY
  decision=makeMove(PLAYERSARRAY, playerOnMove, possibleMoves)
  if decision=="fold":

    newPlayersArray = fold(PLAYERSARRAY, playerOnMove)
    displayPlayers(newPlayersArray, displayedCards)
    if len(newPlayersArray)==1:
      print(f"Wygrywa gracz {newPlayersArray[0]['nick']}")
      return 0
    nextPlayer = setNextPlayer(playerOnMove-1, len(newPlayersArray))
    if biddingStart==False:
      continueBidding(newPlayersArray, nextPlayer, ['fold', 'call', 'raise'], biddingStart)
    else:
      continueBidding(newPlayersArray, nextPlayer, ['check', 'bet', 'fold'], biddingStart)
  elif decision=="call":
    #placeABet(PLAYERSARRAY, playerOnMove, currentBet)
    call(PLAYERSARRAY,playerOnMove)
    displayPlayers(PLAYERSARRAY, displayedCards)
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
      elif bet>MAXBID:
        print(f"Zakład nie może być większy niż {MAXBID}$")
      else:
        break 
    placeABet(PLAYERSARRAY, playerOnMove, bet)
    displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'])
  elif decision=="check":
    global checkNumber
    checkNumber+=1
    if checkNumber==len(PLAYERSARRAY):
      ## koniec etapu licytacji
      return PLAYERSARRAY
    displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['check', 'bet', 'fold'], True)
  elif decision=="bet":
    betMove(PLAYERSARRAY, playerOnMove)
    displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'])
  return PLAYERSARRAY


def startBidding(oryginalArray):
  PLAYERSARRAY = oryginalArray.copy()
  ## ustawienie tablicy playersBets
  setPlayersBetsList(PLAYERSARRAY)
  #print(playersBets)

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
  newPlayersArray = continueBidding(PLAYERSARRAY,playerOnMove, ['fold', 'call', 'raise'])

  return newPlayersArray
  
def beginNextRound(oryginalArray, PLAYERSARRAY, displayedCards):
  ## zaczyna gracz siedzący najbliżej dealer'a
  dealerIndex = 0
  for i in range(len(oryginalArray)):
    if oryginalArray[i]['role']=='D':
      dealerIndex=i
      break
  playerOnMove=None
  for i in range(dealerIndex+1, dealerIndex +1 + len(oryginalArray)):
    for j in range(len(PLAYERSARRAY)):
      if oryginalArray[i%len(oryginalArray)]['id']==PLAYERSARRAY[j]['id']:
        playerOnMove = j
        break
    if playerOnMove is not None:
      break
  # continue bidding
  # wyświetlenie kart
  displayCards(displayedCards)
  continueBidding(PLAYERSARRAY, playerOnMove, ['check', 'bet', 'fold'], True, displayedCards)
  #print(playerOnMove, displayedCards)



