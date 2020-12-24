from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=23
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
cards = []
result = 0

def play_round(cups, idx):

    print("\n-- move {i} --".format(i=str(idx + 1)))

    idx = idx % len(cups)
    og_cups = cups[:]
    og_cup = cups[idx]
    dt = cups[idx] - 1
    print ("current cup: " + str(og_cup))
    print("cups: {c}".format(
        c=" ".join(["({x})".format(x=cups[i]) if i == idx else "{x}".format(x=cups[i]) for i in range(len(cups)) ])
    ))

    pick_up = []

    for i in range(3):
        pick_up.append(cups.pop(idx + 1 if idx + 1 < len(cups) else 0))

    print("pick ups: {p}".format(p=", ".join([str(i) for i in pick_up])))


    
    if dt == 0:
        dt = max(cups)

    while dt in pick_up:
        dt -= 1
        if dt == 0:
            dt = max(cups)

    print(dt)

    dt_idx = cups.index(dt) 

    dest = cups.pop(dt_idx)

    print(cups)
    
    print(dt_idx)

    if dt_idx == 0:
        dt_idx = len(cups)

    print ("destination: " + str(dt))

    cups.insert(dt_idx, dest)

    dt_idx += 1
    
    while len(pick_up) > 0:
        cups.insert(dt_idx, pick_up.pop(0))
        dt_idx += 1

    while og_cup != cups[idx]:
        cups.insert(0, cups.pop())

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

cards = [int(c) for c in lines[0]]

rounds = 100

for i in range(rounds):
    play_round(cards, i)

sIdx = cards.index(1)

result = ''

for i in range(1, len(cards)):
    result += str(cards[(sIdx + i) % len(cards)])


print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")