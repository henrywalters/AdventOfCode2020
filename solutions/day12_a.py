from utils import Timer
from utils import Vec2
from utils import pi
from utils import deg2rad
import math

DAY=12
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

facing = Vec2(1, 0)
pos = Vec2(0, 0)

def parse():
    return [(l[0], int(l[1:len(l)])) for l in lines]

def handle(parsed):
    for x in parsed:
        print(x)
        if x[0] == 'N':
            pos.add(Vec2(0, x[1]))
        elif x[0] == 'S':
            pos.add(Vec2(0, -x[1]))
        elif x[0] == 'E':
            pos.add(Vec2(x[1], 0))
        elif x[0] == 'W':
            pos.add(Vec2(-x[1], 0))
        elif x[0] == 'F':
            pos.add(Vec2(facing.x * x[1], facing.y * x[1]))
        elif x[0] == 'R':
            facing.rotate(-deg2rad(x[1]))
            facing.x = int(facing.x)
            facing.y = int(facing.y)
        elif x[0] == 'L':
            facing.rotate(deg2rad(x[1]))
            facing.x = int(facing.x)
            facing.y = int(facing.y)
        else:
            raise Exception("Invalid key")

        print(pos)
        print(facing)

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