from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=23
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
cards = []
result = 0

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

raw = [int(c) for c in lines[0]]
cups = {}

for i in range(len(raw) - 1):
    cups[raw[i]] = raw[i + 1]
cups[raw[-1]] = max(cups) + 1

print(cups)


print(y, z)

result = x * y

for i in range(1, len(cards)):
    result += str(cards[(sIdx + i) % len(cards)])


print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")