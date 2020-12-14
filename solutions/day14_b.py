from utils import Timer
from utils import Vec2
from utils import pi
import itertools
import math

DAY=14
PART='b'

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
    print (bNum)
    print(mask)
    tmp = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            tmp += '1'
        elif mask[i] == '0':
            tmp += bNum[i]
        elif mask[i] == 'X':
            tmp += 'X'
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
            idx = int(varParts[1][0:len(varParts[1]) - 1])
            print(idx, val)

            adj = apply_mask(cvt2bin(idx, size), mask)
            float_idx = []

            for i in range(len(adj)):
                if adj[i] == 'X':
                    float_idx.append(i)

            bins = [[0, 1] for i in range(len(float_idx))]

            bin_pos = list(itertools.product(*bins))

            print(adj)

            for pos in bin_pos:
                tmp = ''
                f_idx = 0
                for i in range(size):
                    if i in float_idx:
                        tmp += str(pos[f_idx])
                        f_idx += 1
                    else:
                        tmp += adj[i]
                print(pos)
                print(tmp)
                print(bin2int(tmp))
                mem[bin2int(tmp)] = val

            print(bin_pos)
            

            print(adj)

            #mem[idx] = bin2int(apply_mask(cvt2bin(val, size), mask))
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