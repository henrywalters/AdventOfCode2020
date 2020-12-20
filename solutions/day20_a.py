from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=20
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def parse_tiles():
    tiles = []
    idx = None
    tile = []

    for l in lines:
        if 'Tile' in l:
            idx = int(l.split(' ')[1][0:4])
        elif l == '':
            tiles.append({
                'id': idx,
                'tile': tile,
                'edges': get_edges(tile)
            })
            tile = []
        else:
            tile.append(l)

    tiles.append({
        'id': idx,
        'tile': tile,
        'edges': get_edges(tile)
    })

    for t in tiles:
        t['possible'] = get_possible_neighbors(t, tiles)
    
    return tiles

def get_edges(tile):
    ## return a tuple like (top, right, bottom, left)
    size = len(tile[0])
    edges = ([], [], [], [])
    for i in range(size):
        edges[3].append(tile[i][0])
        edges[2].append(tile[size - 1][i])
        edges[1].append(tile[i][size-1])
        edges[0].append(tile[0][i])
    return edges

def get_possible_neighbors(tile, tiles):
    poss = []
    for t in tiles:
        if t['id'] != tile['id']:
            print ("Checking", t['id'])
            for e1 in t['edges']:
                for e2 in tile['edges']:
                    e2r = list(reversed(e2))
                    print(e1, e2, e2r)
                    if e1 == e2 or e1 == e2r:
                        poss.append(t['id'])

    return poss
        

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

tiles = parse_tiles()

print(tiles)

#t = None
#for tile in tiles:
#    if tile['id'] == 2311:
#        t = tile

#poss = get_possible_neighbors(t, tiles)
#print(poss)

corner_ids = [t['id'] if len(t['possible']) == 2 else 1 for t in tiles]

print(corner_ids)

result = pi(corner_ids)

print(len(tiles))

print([len(t['possible']) for t in tiles])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")