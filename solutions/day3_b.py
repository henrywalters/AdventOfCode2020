from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=3
PART='B'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

# check if a map line at index i (adjusted for infinality) is a tree
def is_tree(map, i):
    # Spent way too long on the fact it had extra white space :(
    size = len(map.strip())
    adj_index = i % size
    return map[adj_index] == '#'

def find_tree_hits(lines, delta):
    pos = Vec2(0, 0)
    trees_hit = 0
    while pos.y < len(lines):
        if is_tree(lines[pos.y], pos.x):
            trees_hit += 1
        pos.add(delta)
    return trees_hit

trees_hit = 0

deltas = (
    Vec2(1, 1),
    Vec2(3, 1),
    Vec2(5, 1),
    Vec2(7, 1),
    Vec2(1, 2),
)

with open('files/day3.txt', 'r') as f:
    lines = f.readlines()
    tree_hits = [find_tree_hits(lines, delta) for delta in deltas]
    
print (tree_hits)

print("Trees hit: {f}".format(f=pi(tree_hits)))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")