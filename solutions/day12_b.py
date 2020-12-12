from utils import Timer
from utils import Vec2
from utils import pi
from utils import deg2rad
import math

DAY=12
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

waypoint = Vec2(10, 1)
pos = Vec2(0, 0)

def parse():
    return [(l[0], int(l[1:len(l)])) for l in lines]

def handle(parsed):
    for x in parsed:
        print(x)
        if x[0] == 'N':
            waypoint.add(Vec2(0, x[1]))
        elif x[0] == 'S':
            waypoint.add(Vec2(0, -x[1]))
        elif x[0] == 'E':
            waypoint.add(Vec2(x[1], 0))
        elif x[0] == 'W':
            waypoint.add(Vec2(-x[1], 0))
        elif x[0] == 'F':
            pos.add(Vec2(waypoint.x * x[1], waypoint.y * x[1]))
        elif x[0] == 'R':
            waypoint.rotate(-deg2rad(x[1]))
            waypoint.x = round(waypoint.x)
            waypoint.y = round(waypoint.y)
        elif x[0] == 'L':
            waypoint.rotate(deg2rad(x[1]))
            waypoint.x = round(waypoint.x)
            waypoint.y = round(waypoint.y)
        else:
            raise Exception("Invalid key")

        print(pos)
        print(waypoint)

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

handle(parse())

result = pos.manhattan_distance()

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")