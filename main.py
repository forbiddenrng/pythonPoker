import players
import random
import os
import time
import bid
import cards
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

def startGame():
  giveRoles()
  giveInitialCredits()
  cards.giveCardsToPlayers(PLAYERS, CARDS, NUMBEROFPLAYERS)
  cards.showCardsToPlayers(PLAYERS)
  ## licytacja 1
  newPlayersArray = bid.startBidding(PLAYERS)
  ## pierwsze 3 karty
  communityCards=cards.selectFlop(NUMBEROFPLAYERS, CARDS)
  arrayAfterFlop = bid.beginNextRound(PLAYERS, newPlayersArray, communityCards)
  ## kolejna 4 karta - turn (dodawana jest do community cards)
  turn = cards.selectTurn(NUMBEROFPLAYERS, CARDS)
  communityCards.append(turn)
  arrayAfterTurn = bid.beginNextRound(PLAYERS,arrayAfterFlop, communityCards)
  ## 5 karta river
  river = cards.selectRiver(NUMBEROFPLAYERS, CARDS)
  communityCards.append(river)
  arrayAfterRiver = bid.beginNextRound(PLAYERS, arrayAfterTurn, communityCards)
startGame()



