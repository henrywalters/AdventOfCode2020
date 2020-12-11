from utils import Timer
from utils import Vec2
from utils import pi
from utils import clamp
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

def tick(lines):
    adjusted = []
    rc = len(lines)
    cc = len(lines[0])

    for i in range(rc):
        row = []
        for j in range(cc):
            adj = get_adj_seats(lines, i, j)
            if lines[i][j] == 'L' and adj['occ'] == 0:
                row.append('#')
            elif lines[i][j] == '#' and adj['occ'] >= 4:
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
    if tmp == lines:
        stable = True
    lines = tmp

#print (lines)

result = sum([sum([1 if lines[i][j] == '#' else 0 for j in range(len(lines[i]))]) for i in range(len(lines))])

#print(get_adj_seats(lines, 0, 9))

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")