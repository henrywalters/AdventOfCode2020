from utils import Timer
from utils import Vec2
from utils import pi
from utils import min_tuple_list
import math

DAY=13
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def get_earliest_bus(est, buses):
    waits = []
    ids = []
    for i in buses:
        if i != 'x':
            bus_id = int(i)
            print(bus_id)
            print(math.ceil(est / bus_id) * bus_id - est)
            waits.append((math.ceil(est / bus_id) * bus_id - est, bus_id))
    min_wait = min_tuple_list(waits)
    print(min_wait)
    return min_wait[0] * min_wait[1]

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

est = int(lines[0])
buses = lines[1].split(",")

result = get_earliest_bus(est, buses)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")