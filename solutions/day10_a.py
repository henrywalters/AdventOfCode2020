from utils import Timer
from utils import Vec2
from utils import pi
from utils import get_distribution
import math

DAY=10
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

def get_voltage_distributions(lines):
    differences = []
    curr_voltage = 0
    max_voltage = max([lines[i] for i in range(len(lines))])
    lines.append(max_voltage + 3)
    print (lines)
    while curr_voltage <= max_voltage:
        min_diff = None
        min_idx = None
        tmp_voltage = curr_voltage
        for i in range(len(lines)):
            #print (curr_voltage, lines[i])
            if curr_voltage < lines[i] <= curr_voltage + 3:
                #print ("Valid voltage: {v}".format(v = lines[i]))
                if (min_diff is None or lines[i] - curr_voltage < min_diff):
                    min_diff = lines[i] - curr_voltage
                    min_idx = i
                    tmp_voltage = lines[i]
        curr_voltage = tmp_voltage
        #print(lines[min_idx], min_diff)
        differences.append(min_diff)
    #print(differences)

    return get_distribution(differences)

result = 0

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [int(l.strip()) for l in f.readlines()]

print(lines)

dist = get_voltage_distributions(lines)

print(dist)

result = dist[1] * dist[3]

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")