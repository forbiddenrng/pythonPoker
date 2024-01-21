import evaluation, showdown, json, results, sortHand
playersBets={}
def isBiddingEnd(PLAYERSARRAY):
  global playersBets
  betsSum=[]
  for player in PLAYERSARRAY:
    playerNick=player['nick']
    playerBetsSum=0
    for bet in playersBets[playerNick]:
      playerBetsSum+=bet
    betsSum.append(playerBetsSum)
  firstValue=betsSum[0]
  for i in range(len(betsSum)):
    if betsSum[i] != firstValue:
      return False
  return True


def testIsBiddingEnd():
  global playersBets
  playersArr=[{"nick": "Gracz1", "id": 0},{"nick": "Gracz2", "id": 1},{"nick": "Gracz3", "id": 2}]
  playersBets={"Gracz1": [10, 10],"Gracz2": [20],"Gracz3": [20]}
  assert isBiddingEnd(playersArr) == True
  playersBets={"Gracz1": [10, 10],"Gracz2": [20],"Gracz3": [30]}
  assert isBiddingEnd(playersArr) == False



def testEvaluateHand():
  # 8C TS KC 9H 4S 
  # 7D 2S 5D 3S AC
  assert evaluation.evaluateHand([(14, 'S'), (13, 'S'), (12, 'S'), (11, 'S'), (10, 'S')]) == (9, [14,13,12,11,10])
  assert evaluation.evaluateHand([(14, 'S'), (14, 'C'), (14, 'D'), (14, 'H'), (10, 'S')]) == (7, [14,14,14,14,10])
  assert evaluation.evaluateHand([(14, 'S'), (14, 'C'), (14, 'D'), (10, 'H'), (10, 'S')]) == (6, [14,14,14,10,10])
  assert evaluation.evaluateHand([(3, 'S'), (2, 'S'), (5, 'S'), (9, 'S'), (12, 'S')]) == (5, [12,9,5,3,2])
  assert evaluation.evaluateHand([(3, 'D'), (2, 'S'), (4, 'S'), (5, 'C'), (6, 'H')]) == (4, [6,5,4,3,2])
  assert evaluation.evaluateHand([(3, 'D'), (3, 'S'), (4, 'S'), (5, 'C'), (3, 'H')]) == (3, [5,4,3,3,3])
  assert evaluation.evaluateHand([(3, 'D'), (3, 'S'), (4, 'S'), (4, 'C'), (10, 'H')]) == (2, [10,4,4,3,3])
  assert evaluation.evaluateHand([(3, 'D'), (3, 'S'), (4, 'S'), (6, 'C'), (10, 'H')]) == (1, [10,6,4,3,3])
  assert evaluation.evaluateHand([(2, 'D'), (3, 'S'), (4, 'S'), (6, 'C'), (10, 'H')]) == (0, [10,6,4,3,2])

def testSelectWinner():
  with open("test.json", "r") as file:
    dane=json.load(file)
    test1P=dane["test1Players"]
    test1C=dane["test1Cards"]
    test2P=dane["test2Players"]
    test2C=dane["test2Cards"]
    test3P=dane["test3Players"]
    test3C=dane["test3Cards"]
    test4P=dane["test4Players"]
    test4C=dane["test4Cards"]
    assert showdown.selectWinner(test1P, test1C) == ([2], 0)
    assert showdown.selectWinner(test2P, test2C) == ([1], 1)
    assert showdown.selectWinner(test3P, test3C) == ([1], 1)
    assert showdown.selectWinner(test4P, test4C) == ([1,2], 0)

def testSortResults():
  with open("test.json", "r") as file:
    data= json.load(file)
    testQSort1 = data["testQSort"][0]
    testQSort2 = data["testQSort"][1]
    testQSort3 = data["testQSort"][2]
    assert results.sortResults(testQSort1) == sorted(testQSort1, key=lambda x: x["credits"], reverse=True)
    assert results.sortResults(testQSort2) == sorted(testQSort2, key=lambda x: x["credits"], reverse=True)
    assert results.sortResults(testQSort3) == sorted(testQSort3, key=lambda x: x["credits"], reverse=True)

def testMergeSort():
  array1 = [((0, [14, 10, 4, 3, 2]), 2), ((1, [7, 4, 3, 2, 2]), 1)]
  array2 = [((1, [10, 10, 8, 7, 2]), 2), ((0, [13, 12, 7, 4, 2]), 1), ((2, [8,8,7,7,2]), 3), ((3, [14, 10, 9, 4, 1]), 0)]
  array3 = [((2, [10, 10, 8, 7, 2]), 2), ((0, [13, 12, 7, 4, 2]), 1), ((1, [8,8,7,7,2]), 3)]
  assert sortHand.mergeSort(array1) == sorted(array1, key=lambda x: x[0][0])
  assert sortHand.mergeSort(array2) == sorted(array2, key=lambda x: x[0][0])
  assert sortHand.mergeSort(array3) == sorted(array3, key=lambda x: x[0][0])