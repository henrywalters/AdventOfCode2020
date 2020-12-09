from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=9
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

def is_valid_number(number, preamble):
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            print (preamble[i], preamble[j], number)
            if i != j and preamble[i] + preamble[j] == number:
                return True
    return False

result = 0

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [int(l.strip()) for l in f.readlines()]

size = 25

results = [is_valid_number(lines[i], lines[i - size: i]) for i in range(size, len(lines))]

for i in range(len(results)):
    if not results[i]:
        result = lines[i + size]
        break

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")