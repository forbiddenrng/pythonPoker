import itertools
def evaluateHand(hand):
  value_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  value_dict.update((str(x), x) for x in range(2,10))
  # 8 straight flush  (poker)
  # 7 four of a kind (kareta)
  # 6 full house (full)
  # 5 flush (kolor)
  # 4 straight (strit)
  # 3 three of a kind (trójka)
  # 2 two pair (dwie pary)
  # 1 one pair (para)
  # 0 high card (wysoka karta)

  values=sorted([card[0] for card in hand], reverse=True)
  colors= [card[1] for card in hand]
  flush= all(color==colors[0] for color in colors)
  straight = (values == list(range(values[0], values[0]-5, -1))
                or values == [14, 5, 4, 3, 2])

  if straight and flush:
    return 9, values[1]
  if flush:
    return 5, values
  if straight:
    return 4, values[1]
  
  pairs=[]
  trips=[]
  for value, group in itertools.groupby(values):
    count=sum(1 for _ in group)
    if count==4:
      # kareta 
      return 7, value, values
    elif count==3:
      # trójka
      trips.append(value)
    elif count==2:
      pairs.append(value)


  if trips:
    if pairs: return 6, trips, pairs, values
    else: return 3, trips, pairs, values
  else:
    return len(pairs), pairs, values
  
