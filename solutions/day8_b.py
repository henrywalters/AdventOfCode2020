from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=8
PART='b'

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

    while idx not in idx_ran and idx < len(instructions):
        idx_ran[idx] = True
        if instructions[idx][0] == 'acc':
            accum += instructions[idx][1]
            idx += 1
        elif instructions[idx][0] == 'jmp':
            idx += instructions[idx][1]
        else:
            idx += 1

    return accum

def check_if_terminates(instructions):
    idx_ran = {}
    accum = 0
    idx = 0

    while idx not in idx_ran and idx < len(instructions):
        print (idx)
        idx_ran[idx] = True
        if instructions[idx][0] == 'acc':
            accum += instructions[idx][1]
            idx += 1
        elif instructions[idx][0] == 'jmp':
            idx += instructions[idx][1]
        else:
            idx += 1

    return idx >= len(instructions)


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

instructions = parse_boot_code(lines)

for i in range(len(instructions)):
    instructCopy = instructions.copy()
    terminates = False
    
    print(i)
    print(instructions[i][0])

    if instructions[i][0] == 'nop':
        instructCopy[i] = ['jmp', instructions[i][1]]
        # print(instructCopy)
        print(i)
        print(instructions)
        print(instructCopy)
        if check_if_terminates(instructCopy):
            terminates = True
    if instructions[i][0] == 'jmp':
        instructCopy[i] = ['nop', instructions[i][1]]
        print(i)
        print(instructions)
        print(instructCopy)
        if check_if_terminates(instructCopy):
            terminates = True
    
    if terminates:
        instructions = instructCopy
        break

result = run_instructions(instructions)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")