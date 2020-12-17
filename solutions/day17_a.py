from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=17
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

cubes = {}

def get_cubes():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            cubes[(i, j, 0)] = 1 if lines[i][j] == '#' else 0

def get_neighbors(point):
    neighbors = []
    for i in range(point[0] - 1, point[0] + 2):
        for j in range(point[1] - 1, point[1] + 2):
            for k in range(point[2] - 1, point[2] + 2):
                if (i,j,k) != point:
                    neighbors.append((i, j, k))
    return neighbors

def get_active_neighbors(point):
    neighbors = get_neighbors(point)
    return sum([cubes[neighbor] if neighbor in cubes else 0 for neighbor in neighbors])

def get_bounds(cubes):
    m = [None, None, None]
    M = [None, None, None]

    for p in cubes:
        if m[0] is None or p[0] < m[0]:
            m[0] = p[0]
        if m[1] is None or p[1] < m[1]:
            m[1] = p[1]
        if m[2] is None or p[2] < m[2]:
            m[2] = p[2]

        if M[0] is None or p[0] > M[0]:
            M[0] = p[0]
        if M[1] is None or p[1] > M[1]:
            M[1] = p[1]
        if M[2] is None or p[2] > M[2]:
            M[2] = p[2]

    return (m, M)

def tick(cubes):
    updated = {}
    bounds = get_bounds(cubes)
    
    for i in range(bounds[0][0] - 1, bounds[1][0] + 3):
        for j in range(bounds[0][1] - 1, bounds[1][1] + 3):
            for k in range(bounds[0][2] - 1, bounds[1][2] + 3):
                point = (i, j, k)
                print(point)
                active = get_active_neighbors(point)
                if point in cubes and cubes[point] == 1:
                    if active == 2 or active == 3:
                        updated[point] = 1
                    else:
                        updated[point] = 0
                else:
                    if active == 3:
                        updated[point] = 1
                    else:
                        updated[point] = 0
    return updated

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

get_cubes()

for i in range(6):
    cubes = tick(cubes)
    print (cubes)

result = sum([cubes[p] for p in cubes])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")