players = [1, 2, 3, 4, 5, 6, 7, 8]

def pair(players):
    while len(players) > 0:
        print(str(len(players)))
        del players[0]
        if len(players) == 1:
          del players[0]
        
print(players)

pair(players)
print(players)