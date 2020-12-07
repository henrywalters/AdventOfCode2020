from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=6
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

result = 0

def parse_groups(lines):
    groups = []
    people = []

    for line in lines:
        if line == '':
            groups.append(set.intersection(*[set(person) for person in people]))
            people = []
        else:
            person = []
            for c in line:
                person.append(c)
            people.append(person)

    groups.append(set.intersection(*[set(person) for person in people]))

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