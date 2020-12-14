from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=14
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def cvt2bin(num, max_size):
    return bin(num)[2:].rjust(max_size, '0')

def bin2int(num):
    return int(num, 2)

def apply_mask(bNum, mask):
    tmp = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            tmp += '1'
        elif mask[i] == '0':
            tmp += '0'
        else:
            tmp += bNum[i]
    return tmp

def run_program():
    mask = lines[0].split(' = ')[1]
    size = len(mask)
    mem = {}
    for line in lines:
        if line.split(' = ')[0] == 'mask':
            mask = line.split(' = ')[1]
        else:
            parts = line.split(' = ')
            val = int(parts[1])
            varParts = parts[0].split('[')
            idx = varParts[1][0:len(varParts[1]) - 1]

            mem[idx] = bin2int(apply_mask(cvt2bin(val, size), mask))
    return mem

with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

mem = run_program()

result = sum([mem[i] for i in mem])

print(mem)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")