from utils import Timer
from utils import Vec2
from utils import pi
from utils import print_list, print_dict
import math
import copy

DAY=24
PART='b'

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

def get_neighbors(pos):
    return (
        Vec2(pos.x + 1, pos.y),
        Vec2(pos.x + 1, pos.y + 1),
        Vec2(pos.x, pos.y + 1),
        Vec2(pos.x - 1, pos.y),
        Vec2(pos.x - 1, pos.y - 1),
        Vec2(pos.x, pos.y - 1)
    )

def get_adj_black_tiles(tiles, pos):
    neighbors = get_neighbors(pos)
    blacks = 0
    for n in neighbors:
        if n.get_tuple() in tiles:
            blacks += 1

    return blacks


def get_bounds(tiles):
    m = [None, None]
    M = [None, None]

    for tile in tiles:
        if m[0] is None or tile[0] < m[0]:
            m[0] = tile[0]
        if m[1] is None or tile[1] < m[1]:
            m[1] = tile[1]
        if M[0] is None or tile[0] > M[0]:
            M[0] = tile[0]
        if M[1] is None or tile[1] > M[1]:
            M[1] = tile[1]

    return (m, M)

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]


tiles = {}

for l in lines:
    tile = get_final_tile(l)
    if tile.get_tuple() in tiles:
        tiles[tile.get_tuple()] = not tiles[tile.get_tuple()]
    else:
        tiles[tile.get_tuple()] = True

print_dict(tiles)

print(sum([1 if tiles[tile] else 0 for tile in tiles]))

new_tiles = {}

for tile in tiles:
    if tiles[tile]:
        new_tiles[tile] = True

tiles = new_tiles

print_dict(tiles)

for i in range(100):
    og_tiles = copy.deepcopy(tiles)
    bounds = get_bounds(og_tiles)
    #print_dict(tiles)

    updated = {}

    #print(tiles)

    print(bounds)

    b = 0
    w = 0

    for i in range(bounds[0][0] - 1, bounds[1][0] + 3):
        for j in range(bounds[0][1] - 1, bounds[1][1] + 3):
            tile = (i, j)
            bNeighbors = get_adj_black_tiles(og_tiles, Vec2(i, j))

            if tile in og_tiles:
                if og_tiles[tile] and (bNeighbors == 1 or bNeighbors == 2):
                    updated[tile] = True

            else:
                if bNeighbors == 2:
                    updated[tile] = True

            #if tile in og_tiles and og_tiles[tile] and (bNeighbors == 0 or bNeighbors > 2):
            #    print("Flipped to white")
            #    tiles[(i, j)] = False
            #    w += 1
            #if (tile not in og_tiles or not og_tiles[tile]) and bNeighbors == 2:
            #    print("Flipped to black")
            #    tiles[(i, j)] = True
            #   b += 1

    tiles = updated

    print("B = {b} W = {w}".format(b=b, w=w))

    print(sum([1 if tiles[tile] else 0 for tile in tiles]))

result = sum([1 if tiles[tile] else 0 for tile in tiles])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")