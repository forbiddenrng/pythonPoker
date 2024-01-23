import bid, move, win, display
def continueBidding(PLAYERSARRAY, playerOnMove, possibleMoves, biddingStart=False, displayedCards=[]):
  ## sprawdzenie czy licytacja się nie skończyła -- czy każdy gracz dał tyle samo do puli
  ## jeśli każdy dał tyle samo do puli to licytacja się kończy i przechodzi do następnego etapu.
  global checkNumber
  isEnd=bid.isBiddingEnd(PLAYERSARRAY)
  if isEnd and not biddingStart:
    bid.resetCheck()
    return PLAYERSARRAY
  decision=move.makeMove(PLAYERSARRAY, playerOnMove, possibleMoves)
  if decision=="fold":
    newPlayersArray = bid.fold(PLAYERSARRAY, playerOnMove)
    checkNumber=bid.getCheckNumber()
    if checkNumber==len(newPlayersArray):
      ## koniec etapu licytacji, resetowanie liczby check
      bid.resetCheck()
      return newPlayersArray
    #newPlayersArray = bid.fold(PLAYERSARRAY, playerOnMove)
    display.displayPlayers(newPlayersArray, displayedCards)
    if len(newPlayersArray)==1:
      # wygrywa ostatni gracz, który nie foldował
      return win.handleWinner(PLAYERSARRAY, [newPlayersArray[0]['id']], 0)
    nextPlayer = move.setNextPlayer(playerOnMove-1, len(newPlayersArray))
    if biddingStart==False:
      continueBidding(newPlayersArray, nextPlayer, ['fold', 'call', 'raise'], biddingStart, displayedCards)
    else:
      continueBidding(newPlayersArray, nextPlayer, ['check', 'bet', 'fold'], biddingStart, displayedCards)
  elif decision=="call":
    #placeABet(PLAYERSARRAY, playerOnMove, currentBet)
    bid.resetCheck()
    bid.call(PLAYERSARRAY,playerOnMove)
    display.displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = move.setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'], biddingStart, displayedCards)
  elif decision=="raise":
    bet=0
    bid.resetCheck()
    while True:
      currentBet=bid.getCurrentBet()
      MAXBID=bid.getMaxBid()
      bet = move.getPlayersResponse("Podaj wartość bet'a: ")
      if bet>PLAYERSARRAY[playerOnMove]['credits']:
        print("Nie masz tyle na koncie!!! Podaj mniejszy zakład")
      elif bet<currentBet:
        print("Zakład nie może być mniejszy niż poprezdni!")
      elif bet>MAXBID:
        print(f"Zakład nie może być większy niż {MAXBID}$")
      else:
        break 
    bid.placeABet(PLAYERSARRAY, playerOnMove, bet)
    display.displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = move.setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'], False, displayedCards)
  elif decision=="check":
    bid.updateCheck()
    checkNumber=bid.getCheckNumber()
    if checkNumber==len(PLAYERSARRAY):
      ## koniec etapu licytacji
      ## resetowanie liczby check
      bid.resetCheck()
      return PLAYERSARRAY
    display.displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = move.setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['check', 'bet', 'fold'], True, displayedCards)
  elif decision=="bet":
    bid.resetCheck()
    bid.betMove(PLAYERSARRAY, playerOnMove)
    display.displayPlayers(PLAYERSARRAY, displayedCards)
    nextPlayer = move.setNextPlayer(playerOnMove, len(PLAYERSARRAY))
    continueBidding(PLAYERSARRAY, nextPlayer, ['fold', 'call', 'raise'], False, displayedCards)
  return PLAYERSARRAY
