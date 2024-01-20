import bid, os
from bid import getPot
from bid import currentBet
import cards, sortHand, win
from evaluation import evaluateHand

def showPlayersCards(PLAYERSARRAY):
  for player in PLAYERSARRAY:
    card1N = cards.getCardName(player['cards'][0]['value'])
    card2N = cards.getCardName(player['cards'][1]['value'])
    card1C = player['cards'][0]['color']
    card2C = player['cards'][1]['color']
    nick = player['nick']
    print(f"{nick}: {card1N} {card1C}, {card2N} {card2C}")

def selectWinner(PLAYERSARRAY, communityCards):
  # funkcja zwraca listę id graczy, którzy wygrali - jeśli wygra jeden gracz funkcja zwaraca listę o długości 1
  ## każdemu graczowi przypisywana jest moc układu
  valueDict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  valueDict.update((str(x), x) for x in range(2,10))
  #print(PLAYERSARRAY, communityCards)
  playersHandsValues=[]
  for player in PLAYERSARRAY:
    playerDeck = player['cards'] + communityCards
    playerDeckNewFormat = cards.reformatCards(playerDeck)
    cardsToEvaluate=[(valueDict[card[0]], card[1]) for card in playerDeckNewFormat]
    playerHandValue = evaluateHand(cardsToEvaluate)
    playersHandsValues.append((playerHandValue, player['id']))
  playersHandsValues = sortHand.mergeSort(playersHandsValues)[::-1]
  #print(playersHandsValues)
  # zliczenie ile jest układów o największej mocy 
  bestHandsNumber = 0
  bestHandValue = playersHandsValues[0][0][0]  
  for tuple in playersHandsValues:
    if tuple[0][0]==bestHandValue:
      bestHandsNumber+=1
  #print(playersHandsValues)
  if bestHandsNumber==1:
    # jeden największy układ - jeden zwycięzca
    #print("wygrał gracz o id: ", playersHandsValues[0][1])
    return [playersHandsValues[0][1]], playersHandsValues[0][0][0]
  else:
    # więcej niż jeden gracz ma taki sam, najwyższy układ
    playersHands=[]
    for player in PLAYERSARRAY:
      playerCards=sorted([player['cards'][0]['value'], player['cards'][1]['value']])
      playersHands.append((playerCards[0], playerCards[1], player['id']))
    # sortowanie listy krotek wg. pierwszej wartości
    playersHands.sort(key=lambda x: x[0], reverse=True)
    print(playersHands)
    ## usuwanie wszystkich krotek, które mają na 1 "slocie" inna wartość niż największa krotka
    playersHands=[tuple for tuple in playersHands if tuple[0]==playersHands[0][0]]



    '''for tuple in playersHands:
      if tuple[0]!= playersHands[0][0]:
        playersHands.remove(tuple)'''
    if len(playersHands)==1:
      # wygrywa gracz ktory został w tablicy
      handV=None
      for tuple in playersHandsValues:
        if tuple[1]==playersHands[0][2]:
          handV=tuple[0][0]
      return [playersHands[0][2]], handV
    # # sortowanie listy krotek wg. drugiej wartości
    playersHands.sort(key=lambda x: x[1], reverse=True)
    print(playersHands)
    playersHands=[tuple for tuple in playersHands if tuple[1]==playersHands[0][1]]
    '''for tuple in playersHands:
      if tuple[1] != playersHands[0][1]:
        playersHands.remove(tuple)'''
    if len(playersHands)==1:
      # wygrywa gracz ktory został w tablicy
      handV=None
      for tuple in playersHandsValues:
        if tuple[1]==playersHands[0][2]:
          handV=tuple[0][0]
      return [playersHands[0][2]], handV
    else:
      # gracze mają takie same ręce startowe - remis i podział puli
      handV=None
      for tuple in playersHandsValues:
        if tuple[1]==playersHands[0][2]:
          handV=tuple[0][0]
      return [player[2] for player in playersHands], handV

def showDown(PLAYERSARRAY, communityCards):
  os.system('cls')
  bid.displayPlayers(PLAYERSARRAY, communityCards)
  showPlayersCards(PLAYERSARRAY)
  ## wybranie zwycięzcy
  selectWinnerOutput= selectWinner(PLAYERSARRAY, communityCards)
  winnersArray=selectWinnerOutput[0]
  handValue=selectWinnerOutput[1]
  arrayAfterGame = win.handleWinner(PLAYERSARRAY, winnersArray, handValue)
  return arrayAfterGame
  
