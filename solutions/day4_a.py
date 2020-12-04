from utils import Timer
import re

DAY=4
PART='A'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

def is_valid_passport(passport):
    fields = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    )

    for field in fields:
        if field not in passport:
            return False
    return True

def parse_passports(lines):
    passports = []
    curr_passport = {}
    for i in range(len(lines)):
        if lines[i].strip() == '':
            passports.append(curr_passport)
            curr_passport = {}
        else:
            parts = lines[i].split(' ')
            for part in parts:
                field = part.split(':')
                curr_passport[field[0]] = field[1].strip()
    passports.append(curr_passport)
    return passports

with open('files/day4.txt', 'r') as f:
    lines = f.readlines()
    passports = parse_passports(lines)
    valids = 0
    for passport in passports:
        print(passport)
        if is_valid_passport(passport):
            valids += 1

print ("Valid passports: {y}".format(y=valids))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")