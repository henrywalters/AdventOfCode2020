from utils import Timer

DAY=2
PART='A'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

with open('files/day2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)


# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")