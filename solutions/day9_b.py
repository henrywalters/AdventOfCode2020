from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=9
PART='b'

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

def find_weakness(number, lines):
    set_size = 2
    weakness = None

    while set_size < len(lines) and weakness is None:
        for i in range(set_size, len(lines)):
            # print(lines[i - set_size: i])
            if sum(lines[i - set_size: i]) == number:
                weakness = lines[i - set_size: i]
        set_size += 1

    return weakness

result = 0

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [int(l.strip()) for l in f.readlines()]

size = 25

index = 0
results = [is_valid_number(lines[i], lines[i - size: i]) for i in range(size, len(lines))]

for i in range(len(results)):
    if not results[i]:
        index = i
        result = lines[i + size]
        break

# print (index)

weakness = find_weakness(result, lines)

print(weakness)

result = min(weakness) + max(weakness)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")