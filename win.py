import cards
from bid import getPot
def handleWinner(PLAYERSARRAY, winnersArray, handValue):
  newPlayersArray= PLAYERSARRAY.copy()
  handName=cards.getHandName(handValue)
  print(handValue, handName)
  pot=getPot()
  if len(winnersArray)==1:
    nick=""
    for player in newPlayersArray:
      if player['id']==winnersArray[0]:
        nick=player['nick']
    print(f"Wygrywa gracz: {nick}. Układ to: {handName}. Wygrana: {pot}$")
  else:
    winnersNicks=[]
    for player in newPlayersArray:
      for winner in winnersArray:
        if player['id']==winner:
          winnersArray.append(player['nick'])
    winnersString = ", ".join(winnersNicks)
    print(f"Zwycięzcy: {winnersString}. Układ to {handName}. Wygrana: {pot//len(winnersArray)}$")

  for player in newPlayersArray:
    for winner in winnersArray:
      if player['id'] == winner:
        player['credits']+=(pot//len(winnersArray))
  
  return newPlayersArray

