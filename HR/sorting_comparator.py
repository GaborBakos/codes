'''
    Given an array of  Player objects, write a comparator that sorts them in order of decreasing score.
    If  or more players have the same score, sort those players alphabetically ascending by name.
    To do this, you must create a Checker class that implements the Comparator interface, then write an 
    int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.
    In short, when sorting in ascending order, a comparator function returns -1 if a < b, 
    0 if a = b, and 1 if a > b.
    EXAMPLE:
    3 players
    DATA = [[Smith, 20], [Jones, 15], [Jones, 20]]
    OUTPUT = [[Jones, 20], [Smith,20], [Jones, 15]]
'''



from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name > b.name:
                return 1
            else:
                return -1

print('TESTING')
print('''Input:
5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150
''')

print('''Expected Output:
aleksa 150
amy 100
david 100
aakansha 75
heraldo 50
''')


ins = [['amy', 100], ['david', 100], ['herlando', 50], ['aakansha', 75], ['aleksa', 150]]
n = 5
data = []
for i in range(n):
    name, score = ins[i]
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


    
