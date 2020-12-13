from utils import Timer
from utils import Vec2
from utils import pi
from utils import min_tuple_list
from utils import chinese_remainder_theorem
import math

DAY=13
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def adjusted_departure_times(buses):
    times = []
    for i in range(len(buses)):
        if buses[i] != 'x':
            times.append((int(buses[i]), i))
    return times

def is_valid_ts(times, ts):
    for t in times:
        offset = math.ceil(ts / t[0]) * t[0] - ts
        if offset != t[1]:
            return False
    return True

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

est = int(lines[0])
buses = lines[1].split(",")

times = adjusted_departure_times(buses)

valid_ts = None

#ts = 0
#while valid_ts is None:
#    if is_valid_ts(times, ts):
#        valid_ts = ts
#    ts += times[0][0]
#    print(ts)

#result = valid_ts

buses = [(-i,int(b)) for i,b in enumerate(buses) if b != "x"]

result = chinese_remainder_theorem(buses)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")