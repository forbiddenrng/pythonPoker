import json

# zapisywanie tablicy graczy do pliku
def savePlayersArray(array):
  with open("results.json", "w") as f:
    json.dump(array, f)

def readResults():
  with open("results.json", "r") as file:
    results=json.load(file)
    ## sortowanie results według ilości kredytów