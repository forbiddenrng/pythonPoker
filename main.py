import players
import random
import os
import time
import bid
CARDS=[]
colors = ["pik", "trefl", "karo", "kier"]
for color in colors:
  for i in range(2,15):
    CARDS.append({
      "color": color,
      "value": i,
    })
PLAYERS = []
firstGame=True
INITIALCREDITS=500

NUMBEROFPLAYERS = 4
PLAYERS = players.getPlayers(NUMBEROFPLAYERS)

roles = ["D", "SB", "BB", ""]
def giveRoles():
  randomPlayerIndex = random.randint(0,NUMBEROFPLAYERS-1)
  mainRolesCounter = 0
  for i in range(NUMBEROFPLAYERS):
    if mainRolesCounter < 3:
      PLAYERS[(i+randomPlayerIndex)%NUMBEROFPLAYERS]['role'] = roles[mainRolesCounter]
      mainRolesCounter+=1
    else:
      PLAYERS[(i+randomPlayerIndex)%NUMBEROFPLAYERS]['role'] = ""

def giveInitialCredits():
  if firstGame:
    for player in PLAYERS:
      player['credits']=INITIALCREDITS

def giveCardsToPlayers():
  #tasowanie
  random.shuffle(CARDS)
  cardsIndex=0
  for j in range(NUMBEROFPLAYERS):
    PLAYERS[j]['cards'] = [CARDS[cardsIndex], CARDS[cardsIndex+1]]
    cardsIndex+=2
  
def showCardsToPlayers():
  for player in PLAYERS:
    card1Value=player['cards'][0]['value']
    card2Value=player['cards'][1]['value']
    card1Name=""    
    card2Name=""
    card1Name=card1Value    
    card2Name=card2Value    
    if card1Value>10:
      if card1Value == 11:
        card1Name="J"
      elif card1Value == 12:
        card1Name="Q"
      elif card1Value == 13:
        card1Name="K"
      elif card1Value == 14:
        card1Name="A"
    if card2Value>10:
      if card2Value == 11:
        card2Name="J"
      elif card2Value == 12:
        card2Name="Q"
      elif card2Value == 13:
        card2Name="K"
      elif card2Value == 14:
        card2Name="A"

    playersCards = f"{card1Name} {player['cards'][0]['color']}, {card2Name} {player['cards'][1]['color']}"
    print(f"{player['nick']} {player['role']}: {playersCards}")
    time.sleep(1)
    os.system('cls')

def startGame():
  giveRoles()
  giveInitialCredits()
  giveCardsToPlayers()
  showCardsToPlayers()
  bid.startBidding(PLAYERS)

startGame()



