from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=20
PART='b'

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
            ## Return a tuplie like (id, i, j, xFlip, yFlip)
            for i in range(4):
                for j in range(4):
                    print(tile['id'], t['id'])
                    e1 = tile['edges'][i]
                    e2 = t['edges'][j]
                    edge_matches = (
                        (0, 2),
                        (1, 3),
                        (2, 2),
                        (3, 0)
                    )

                    x_flip_matches = (
                        (1, 1),
                        (3, 3),
                    )

                    y_flip_matches = (
                        (2, 2),
                        (0, 0),
                    )
                    if e1 == e2 and (i, j) in edge_matches:
                        poss.append((t['id'], i, j, False, False))

                    if e1 == e2 and (i, j) in x_flip_matches:
                        poss.append((t['id'], i, j, True, False))

                    if e1 == e2 and (i, j) in y_flip_matches:
                        poss.append((t['id'], i, j, False, True))

                    #e2r = list(reversed(e2))
                    #if e1 == e2r:
                        #poss.append((t['id'], i, j, True))

    return poss
        

def arrange_tiles(tile_map):
    T = []
    start_tile = None
    for idx in tile_map:
        t = tile_map[idx]
        if len(t['possible']) == 2:
            e1 = t['possible'][0]
            e2 = t['possible'][1]

            print(t['id'], e1, e2)

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

tiles = parse_tiles()

print(tiles)

tile_map = {}

for t in tiles:
    tile_map[t['id']] = t

arrange_tiles(tile_map)

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