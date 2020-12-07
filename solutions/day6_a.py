from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=6
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

result = 0

def parse_groups(lines):
    groups = []
    group = []

    for line in lines:
        if line == '':
            groups.append(group)
            group = []
            people = []
        else:
            for c in line:
                if c not in group:
                    group.append(c)
    if len(group) > 0:
        groups.append(group)
    return groups

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

groups = parse_groups(lines)

result = sum([len(group) for group in groups])

print(groups)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")