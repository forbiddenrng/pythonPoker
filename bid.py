import os, cards, move, win, bidding, display
SMALLBLIND = 10
currentBet= 0
pot=0
MAXBID=200
checkNumber=0
playersBets={
  
}
def getSB(): return SMALLBLIND
def getCheckNumber(): return checkNumber
def getCurrentBet(): return currentBet
def getMaxBid(): return MAXBID  

def resetPlayersBets():
  global playersBets
  playersBets = {}
def resetBet():
  global currentBet
  currentBet=0
def resetPot():
  global pot
  pot=0

def getPot(): return pot 

def updateCheck():
  global checkNumber
  checkNumber+=1

def setPlayersBetsList(PLAYERSARRAY):
  for player in PLAYERSARRAY:
    playersBets[player['nick']]=[]

def resetCheck():
  global checkNumber
  checkNumber=0


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

def fold(PLAYERSARRAY, playerIndex):
  popPlayer = PLAYERSARRAY.pop(playerIndex)
  return PLAYERSARRAY

def call(PLAYERSARRAY, playerOnMove):
  betToCall=0
  ### sprawdzenie ile ostatni gracz wrzucił łącznie do puli
  prevPlayer = move.getPrevPlayer(PLAYERSARRAY, playerOnMove)
  prevPlayerBetsSum= getPlayersBetsSum(PLAYERSARRAY, prevPlayer)
  currentPlayerBetsSum = getPlayersBetsSum(PLAYERSARRAY, playerOnMove)
  betToCall=prevPlayerBetsSum-currentPlayerBetsSum

  placeABet(PLAYERSARRAY, playerOnMove, betToCall)
  #nextPlayer = setNextPlayer(playerOnMove, len(PLAYERSARRAY))


def betMove(PLAYERSARRAY, playerOnMove):
  bet=0
  while bet>MAXBID or bet<=0 or bet>PLAYERSARRAY[playerOnMove]['credits']:
    bet = move.getPlayersResponse("Podaj wartość bet'a: ")
  os.system('cls')
  placeABet(PLAYERSARRAY, playerOnMove, bet)
  global currentBet
  currentBet=bet



