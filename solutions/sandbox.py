from utils import Timer, Vec2, pi, get_distribution, fibb, fibb_numbers, fibb_recursive, time_fn
import math

DAY=4
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

TEST_SIZE = 100000

time_fn("generate fibb numbers", lambda : fibb_numbers(TEST_SIZE))
time_fn("generate fbb number", lambda : fibb(TEST_SIZE))
#time_fn("Generate fibb numbers recursively", lambda : fibb_recursive(TEST_SIZE))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")