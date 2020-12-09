from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=8
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

result = 0

def parse_boot_code(lines):
    instructions = []
    for line in lines:
        parts = line.split(' ')
        instructions.append((parts[0], int(parts[1])))
    return instructions

def run_instructions(instructions):
    idx_ran = {}
    accum = 0
    idx = 0

    while idx not in idx_ran:
        print(idx)
        idx_ran[idx] = True
        if instructions[idx][0] == 'acc':
            accum += instructions[idx][1]
            idx += 1
        elif instructions[idx][0] == 'jmp':
            idx += instructions[idx][1]
        else:
            idx += 1
        

    return accum


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

instructions = parse_boot_code(lines)

print(instructions)

result = run_instructions(instructions)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")