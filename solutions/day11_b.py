from utils import Timer
from utils import Vec2
from utils import pi
from utils import clamp, in_bounds
import math

DAY=11
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

result = 0

def get_adj_seats(lines, row, col):
    adj = {
        'occ': 0,
        'emp': 0,
    }
    rc = len(lines)
    cc = len(lines[0])
    for i in range(clamp(row - 1, 0, rc), clamp(row + 1, 0, rc - 1) + 1):
        for j in range(clamp(col - 1, 0, cc), clamp(col + 1, 0, cc - 1) + 1):
            if i != row or j != col:
                if lines[i][j] == '#':
                    adj['occ'] += 1
                elif lines[i][j] == 'L':
                    adj['emp'] += 1
    return adj

def get_adj_seats_in_site(lines, row, col):
    adj = {
        'occ': 0,
        'emp': 0,
    }

    dirs = {
        (0, 1): None,
        (1, 1): None,
        (1, 0): None,
        (1, -1): None,
        (0, -1): None,
        (-1, -1): None,
        (-1, 0): None,
        (-1, 1): None
    }

    for i in range(1, max([len(lines), len(lines[0])])):
        needs_update = False
        for d in dirs:
            idx = (row + d[0] * i, col + d[1] * i)
            if dirs[d] is None and in_bounds(lines, idx[0], idx[1]):
                needs_update = True
                if lines[idx[0]][idx[1]] in ['#', 'L']:
                    dirs[d] = lines[idx[0]][idx[1]]
                    updated = True
        if not needs_update:
            break
        

    for d in dirs:
        if dirs[d] == '#':
            adj['occ'] += 1
        if dirs[d] == 'L':
            adj['emp'] += 1

    return adj
            

def tick(lines):
    adjusted = []
    rc = len(lines)
    cc = len(lines[0])

    for i in range(rc):
        row = []
        for j in range(cc):
            adj = get_adj_seats_in_site(lines, i, j)
            if lines[i][j] == 'L' and adj['occ'] == 0:
                row.append('#')
            elif lines[i][j] == '#' and adj['occ'] >= 5:
                row.append('L')
            else:
                row.append(lines[i][j])
        adjusted.append(row)

    return adjusted

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]


stable = False

while not stable:
    tmp = tick(lines)
    print(lines)
    if tmp == lines:
            stable = True
    lines = tmp
    

result = sum([sum([1 if lines[i][j] == '#' else 0 for j in range(len(lines[i]))]) for i in range(len(lines))])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")