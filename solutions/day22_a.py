from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=22
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def play_round(p1, p2):
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    
    if c1 > c2:
        print("Player 1 wins")
        p1.append(c1)
        p1.append(c2)
    else:
        print("Player 2 wins")
        p2.append(c2)
        p2.append(c1)


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

bp = lines.index('')
p1 = [int(x) for x in lines[1:bp]]
p2 = [int(x) for x in lines[bp + 2:]]

while len(p1) > 0 and len(p2) > 0:
    play_round(p1, p2)

winning_hand = list(reversed(p1 if len(p1) > 0 else p2))

result = sum([(i + 1) * winning_hand[i] for i in range(len(winning_hand))])

print(winning_hand)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")