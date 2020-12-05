from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=5
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

def parse_ticket(line):
    row = line[0:7]
    col = line[7:len(line)]
    
    m = 0
    M = 127
    col_id = 0
    row_id = 0
    seat_id = 0

    c = 0
    C = 7

    for i in range(len(row)):
        if row[i] == 'F':
            M = math.floor(((M - m) / 2) + m)
            row_id = m
        else:
            m = math.ceil(M - ((M - m) / 2))
            row_id = M

    for i in range(len(col)):
        if (col[i] == 'L'):
            C = math.floor(((C - c) / 2) + c)
            col_id = c
        else:
            c = math.ceil(C - ((C - c)/ 2))
            col_id = C

    seat_id = row_id * 8 + col_id

    return {
        'col_id': col_id,
        'row_id': row_id,
        'seat_id': seat_id,
    }

result = 0

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

tickets = sorted([parse_ticket(l)['seat_id'] for l in lines])

min_ticket = min(tickets)
max_ticket = max(tickets)

start = min_ticket

for i in range(1, len(tickets)):
    if tickets[i] - tickets[i - 1] > 1:
        result = start + i

print(len(tickets))
print(max_ticket - min_ticket)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")