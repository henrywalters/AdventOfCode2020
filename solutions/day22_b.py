from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=22
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def play_game(p1, p2, game = 1):
    r = 1
    rounds = []
    while len(p1) > 0 and len(p2) > 0:

        for R in rounds:
            if R[0] == p1 and R[1] == p2:
                return True
        
        rounds.append((p1[:], p2[:]))
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if len(p1[0:]) >= c1 and len(p2[0:]) >= c2:
            p1_wins = play_game(p1[0:c1], p2[0:c2], game + 1)
            if p1_wins:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        r += 1
    return True if len(p1) > 0 else False


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

bp = lines.index('')
p1 = [int(x) for x in lines[1:bp]]
p2 = [int(x) for x in lines[bp + 2:]]

p1_wins = play_game(p1, p2)

winning_hand = list(reversed(p1 if len(p1) > 0 else p2))

result = sum([(i + 1) * winning_hand[i] for i in range(len(winning_hand))])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")