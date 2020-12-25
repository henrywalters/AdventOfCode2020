from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=25
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def get_the_bread():
    print(lines)

def transform_subject(subj, loop_size):
    val = 1
    for i in range(loop_size):
        val *= subj
        val %= 20201227
    return val

def get_loop_size(subj, pub_key):
    val = 1
    loop_size = 0
    while val != pub_key:
        val *= subj
        val %= 20201227
        loop_size += 1

    return loop_size

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

card_pub = int(lines[0])
door_pub = int(lines[1])

result = transform_subject(card_pub, get_loop_size(7, door_pub))

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")