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
        if not field in passport:
            print("Invalid")
            return False
        if field == 'byr':
            if len(passport[field]) != 4 or int(passport[field]) < 1920 or int(passport[field]) > 2002:
                print ("Invalid byr")
                return False
        elif field == 'iyr':
            if len(passport[field]) != 4 or int(passport[field]) < 2010 or int(passport[field]) > 2020:
                print ("Invalid iyr")
                return False
        elif field == 'eyr':
            if len(passport[field]) != 4 or int(passport[field]) < 2020 or int(passport[field]) > 2030:
                print ("Invalid eyr")
                return False
        elif field == 'hgt':
            if passport[field][0:len(passport[field]) - 2] == '':
                print("Invalid height")
                return False
            height = int(passport[field][0:len(passport[field]) - 2])
            print(height)
            if 'cm' in passport[field]:
                if (height < 150 or height > 193):
                    print("Invalid height")
                    return False
            elif 'in' in passport[field]:
                if (height < 59 or height > 76):
                    print("Invalid height")
                    return False
            else:
                print("Invalid height")
                return False
        elif field == 'hcl':
            if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport[field]):
                print("Invalid hair color")
                return False
        elif field == 'ecl':
            if not passport[field] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
        elif field == 'pid':
            if not re.search(r'\b\d{9}\b', passport[field]):
                print ("Invalid pid")
                return False


    print("Valid")
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