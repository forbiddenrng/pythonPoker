import players , cards, showdown, bid, results, move, startround
import random
import os
import time
CARDS=[]
colors = ["pik", "trefl", "karo", "kier"]
for color in colors:
  for i in range(2,15):
    CARDS.append({
      "color": color,
      "value": i,
    })
PLAYERSLIST = []
firstGame=True
INITIALCREDITS=500
NUMBEROFPLAYERS = 4
PLAYERSLIST = players.getPlayers(NUMBEROFPLAYERS)
dealerPlayerIndex=None
roles = ["D", "SB", "BB", ""]
def giveRoles(index, PLAYERS):
  #randomPlayerIndex = random.randint(0,NUMBEROFPLAYERS-1)
  mainRolesCounter = 0
  for i in range(NUMBEROFPLAYERS):
    if mainRolesCounter < 3:
      PLAYERS[(i+index)%NUMBEROFPLAYERS]['role'] = roles[mainRolesCounter]
      mainRolesCounter+=1
    else:
      PLAYERS[(i+index)%NUMBEROFPLAYERS]['role'] = ""
  return PLAYERS

def giveInitialCredits():
  if firstGame:
    for player in PLAYERSLIST:
      player['credits']=INITIALCREDITS

def initializeNewGame(arrayAfterShowDown):
  # zmiana roli, dodanie graczy, którzy zrobili fold, dodanie kredytów
  arrayForNextRound=PLAYERSLIST.copy()
  for player in arrayForNextRound:
    for prevPlayer in arrayAfterShowDown:
      if player['id']==prevPlayer['id']:
        player['credits']==prevPlayer['credits']
  
  for player in arrayForNextRound:
    if player['credits']<300:
      print(f"Gracz {player['nick']} nie ma wystarczająco $$ - Koniec gry")
      results.readResults()
      return 0
  
  dealerIndex = (dealerPlayerIndex+1)%NUMBEROFPLAYERS
  giveRoles(dealerIndex, arrayForNextRound)
  bid.resetBet()
  bid.resetPot()
  bid.resetPlayersBets()
  bid.resetCheck()
  startGame(arrayForNextRound, False)

def startGame(PLAYERS, firstGame):
  global dealerPlayerIndex
  if firstGame:
    dealerPlayerIndex = random.randint(0,NUMBEROFPLAYERS-1)
    giveInitialCredits()

  giveRoles(dealerPlayerIndex, PLAYERS)
  cards.giveCardsToPlayers(PLAYERS, CARDS, NUMBEROFPLAYERS)
  cards.showCardsToPlayers(PLAYERS)
  ## licytacja 1
  newPlayersArray = startround.startBidding(PLAYERS)
  ## pierwsze 3 karty
  communityCards=cards.selectFlop(NUMBEROFPLAYERS, CARDS)
  arrayAfterFlop = startround.beginNextRound(PLAYERS, newPlayersArray, communityCards)
  ## kolejna 4 karta - turn (dodawana jest do community cards)
  turn = cards.selectTurn(NUMBEROFPLAYERS, CARDS)
  communityCards.append(turn)
  arrayAfterTurn = startround.beginNextRound(PLAYERS,arrayAfterFlop, communityCards)
  ## 5 karta river
  river = cards.selectRiver(NUMBEROFPLAYERS, CARDS)
  communityCards.append(river)
  arrayAfterRiver = startround.beginNextRound(PLAYERS, arrayAfterTurn, communityCards)
  ## zakonczenie licytacji - showdown
  arrayAfterShowDown = showdown.showDown(arrayAfterRiver, communityCards)
  # zapisać wyniki do pliku
  results.savePlayersArray(arrayAfterShowDown, PLAYERSLIST)
  ## grać dalej czy nie?
  response=0
  while True:
    response=move.getPlayersResponse("Czy chcesz grać dalej? TAK-1; NIE-2: ")
    if response==1 or response==2:
      break
    else:
      print("Wybierz 1 albo 2")
  if response==2:
    # koniec gry, wyświetlenie wyników
    results.readResults()
  elif response==1:
    ## gracze mają wystarczająco kredytów do dalszej gry
    os.system('cls')
    initializeNewGame(arrayAfterShowDown)
        
startGame(PLAYERSLIST, True)