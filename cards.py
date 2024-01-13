import time, os, random
## wybranie 3 kart wspólnych
def selectFlop(numberOfPlayers, cards):
  index=numberOfPlayers*2 ## od tego indexu wybierany jest flop
  return [cards[index], cards[index+1] , cards[index+2]]

def selectTurn(numberOfPlayers, cards):
  # po 2 karty dla gracza + 3 karty z flopa (od indexu 2*numberofplayers + 3)
  # [G1 G1, G2 G2, G3 G3, G4 G4, F F F, T, R]
  index = numberOfPlayers*2 + 3
  return cards[index]

def selectRiver(numberOfPlayers, cards):
  index = numberOfPlayers*2 + 4
  return cards[index]

def giveCardsToPlayers(PLAYERS, CARDS, NUMBEROFPLAYERS):
  #tasowanie
  random.shuffle(CARDS)
  cardsIndex=0
  for j in range(NUMBEROFPLAYERS):
    PLAYERS[j]['cards'] = [CARDS[cardsIndex], CARDS[cardsIndex+1]]
    cardsIndex+=2
  
def getCardName(cardValue):
  if cardValue == 11:
    return "J"
  elif cardValue == 12:
    return "Q"
  elif cardValue == 13:
    return "K"
  elif cardValue == 14:
    return "A"
  else:
    return f"{cardValue}"



def showCardsToPlayers(PLAYERS):
  for player in PLAYERS:
    card1Value=player['cards'][0]['value']
    card2Value=player['cards'][1]['value']

    card1Name= getCardName(card1Value)
    card2Name= getCardName(card2Value)
    
    playersCards = f"{card1Name} {player['cards'][0]['color']}, {card2Name} {player['cards'][1]['color']}"
    print(f"{player['nick']} {player['role']}: {playersCards}")
    time.sleep(1)
    os.system('cls')