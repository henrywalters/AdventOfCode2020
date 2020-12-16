from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=15
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

result = 0

puzzle_input = [2,0,1,9,5,19]

print(puzzle_input)

nums = {}
prev_num = None

size = len(puzzle_input)

idx = 0

last_num = None

while idx < 30000000:
    # tuple = (idx, prev_idx, counts)
    num = None
    if idx < size:
        num = puzzle_input[idx]
        nums[num] = (idx, None, 1)
    else:
        if nums[prev_num][2] == 1:
            num = 0
            nums[num] = (idx, nums[num][0], nums[num][2] + 1)
        else:
            num = nums[prev_num][0] - nums[prev_num][1]
            if num in nums:
                nums[num] = (idx, nums[num][0], nums[num][2] + 1)
            else:
                nums[num] = (idx, None, 1)
    prev_num = num
    last_num = num
    idx += 1

print (last_num)


print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")