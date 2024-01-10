## pobranie nazw graczy i zapisanie ich do bazy
import json

## tworzenie graczy
def createPlayers(numberOfPlayers):
  players=[]
  for i in range(numberOfPlayers):
    nick = input("Podaj nazwe gracza: ")
    players.append({
      "nick": nick,
      "id": i
    })
  return players

## zapisuje dane graczy do pliku
def savePlayersData(playersDict):
  with open("players.json", "w") as file:
    json.dump(playersDict, file)
  

def getPlayers(numberOfPlayers):
  with open("players.json", "r") as file:
    data = json.load(file)
  
  ## jeśli nie ma graczy zapisanych w bazie to stwórz ich i zapisz do pliku
  
  if len(data) == 0:
    data = createPlayers(numberOfPlayers)
    savePlayersData(data)
  
  return data



