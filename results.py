import json, display

# zapisywanie tablicy graczy do pliku
def savePlayersArray(arrayAfterGame, oryginalArray):
  array = []
  for player in oryginalArray:
    array.append({"nick": player['nick'], "id": player['id'], "credits": player['credits']})
  for player in array:
    for playerAG in arrayAfterGame:
      if player['id']==playerAG['id']:
        player['credits']==playerAG['credits'] 
  with open("results.json", "w") as f:
    json.dump(array, f)

def readResults():
  with open("results.json", "r") as file:
    results=json.load(file)
    sortedResults=sortResults(results)
    display.displayResults(sortedResults)
    ## sortowanie results według ilości kredytów

def sortResults(data):
  if len(data)<=1:
    return data
  pivot = data[len(data)-1]['credits']
  higher = [player for player in data if player['credits']>pivot]
  equal = [player for player in data if player['credits']==pivot]
  less = [player for player in data if player['credits']<pivot]

  return sortResults(higher) + equal + sortResults(less)

