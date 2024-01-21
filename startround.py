import bid, move, display, bidding, os
SMALLBLIND=bid.getSB()
def startBidding(oryginalArray):
  PLAYERSARRAY = oryginalArray.copy()
  ## ustawienie tablicy playersBets
  bid.setPlayersBetsList(PLAYERSARRAY)

  playerOnMove=0
  for i in range(len(PLAYERSARRAY)):
    if PLAYERSARRAY[i]['role']=='SB':
      playerOnMove=i
      break
  
  bid.placeABet(PLAYERSARRAY, playerOnMove, SMALLBLIND) ## small blind
  playerOnMove = move.setNextPlayer(playerOnMove, len(PLAYERSARRAY))
  bid.placeABet(PLAYERSARRAY, playerOnMove, 2*SMALLBLIND) ## big blind
  playerOnMove = move.setNextPlayer(playerOnMove, len(PLAYERSARRAY))
  display.displayPlayers(PLAYERSARRAY)
  newPlayersArray = bidding.continueBidding(PLAYERSARRAY,playerOnMove, ['fold', 'call', 'raise'])

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
  os.system('cls')
  bid.resetCheck()
  display.displayPlayers(PLAYERSARRAY, displayedCards)
  newPlayersArray = bidding.continueBidding(PLAYERSARRAY, playerOnMove, ['check', 'bet', 'fold'], True, displayedCards)
  return newPlayersArray