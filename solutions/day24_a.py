from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=24
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def get_final_tile(path):
    options = ('e', 'se', 'sw', 'w', 'nw', 'ne')

    start = Vec2(0, 0)

    cur = ''

    for c in path:
        cur += c
        if cur in options:
            if cur == 'e':
                start.add(1, 0)
            elif cur == 'se':
                start.add(1, 1)
            elif cur == 'sw':
                start.add(0, 1)
            elif cur == 'w':
                start.add(-1, 0)
            elif cur == 'nw':
                start.add(-1, -1)
            elif cur == 'ne':
                start.add(0, -1)
            cur = ''

    return start
        

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]


tiles = {}

for l in lines:
    tile = get_final_tile(l)
    if tile.get_tuple() in tiles:
        tiles[tile.get_tuple()] = not tiles[tile.get_tuple()]
    else:
        tiles[tile.get_tuple()] = True

result = sum([1 if tiles[tile] else 0 for tile in tiles])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")