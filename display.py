import cards, bid, os
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
  print(f"W puli aktualnie jest: {bid.getPot()}$")
  print(f"Wysokość ostatniego zakładu: {bid.getCurrentBet()}$")
  displayCards(displayedCards)

def displayResults(results):
  os.system('cls')
  print("WYNIKI GRY:")
  for i in range(len(results)):
    print(f"{i+1}. {results[i]['nick']}: {results[i]['credits']}$")
