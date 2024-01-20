import time, os, random
## wybranie 1 karty wspólnej
def selectFlop(numberOfPlayers, cards):
  index=numberOfPlayers*2 ## od tego indexu wybierany jest flop
  return [cards[index]]

def selectTurn(numberOfPlayers, cards):
  # 2 karta wspólna
  # [G1 G1, G2 G2, G3 G3, G4 G4, F F F, T, R]
  index = numberOfPlayers*2 + 1
  return cards[index]

def selectRiver(numberOfPlayers, cards):
  # 3 karta wspólna
  index = numberOfPlayers*2 + 2
  return cards[index]

def giveCardsToPlayers(PLAYERS, CARDS, NUMBEROFPLAYERS):
  #tasowanie
  print(PLAYERS)
  random.shuffle(CARDS)
  cardsIndex=0
  for j in range(NUMBEROFPLAYERS):
    if 'cards' in PLAYERS[j]:
      PLAYERS[j]['cards'].clear()
      PLAYERS[j]['cards'].append(CARDS[cardsIndex])
      PLAYERS[j]['cards'].append(CARDS[cardsIndex+1])
    else:
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

def reformatCards(cards):
  # Format = 'VC' 
  # V - wartośc karty of 2 do 14
  # C - kolor karty (S,C,D,H)
  newCards=[]
  for card in cards:
    cardValue, cardColor = str(card['value']), ''
    if card['value']>=10:
      if card['value']==10:
        cardValue='T'
      elif card['value']==11:
        cardValue='J'
      elif card['value']==12:
        cardValue='Q'
      elif card['value']==13:
        cardValue='K'
      elif card['value']==14:
        cardValue='A'
    if card['color']=="pik":
      cardColor+='S'
    elif card['color']=="trefl":
      cardColor+='C'
    elif card['color']=="karo":
      cardColor+='D'
    elif card['color']=="kier":
      cardColor+='H'
    newCards.append((cardValue, cardColor))
  return newCards

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

def getHandName(handValue):
  if handValue==0: return "Wysoka karta"
  elif handValue==1: return "Para"
  elif handValue==2: return "Dwie Pary"
  elif handValue==3: return "Trójka"
  elif handValue==4: return "Strit"
  elif handValue==5: return "Kolor"
  elif handValue==6: return "Full"
  elif handValue==7: return "Kareta"
  elif handValue==9: return "Poker"
