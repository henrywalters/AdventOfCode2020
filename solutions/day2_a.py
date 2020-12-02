from utils import Timer

DAY=2
PART='A'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

def parse_line(line):
    parts = line.split(':')
    policyParts = parts[0].split(' ')
    quantParts = policyParts[0].split('-')

    return {
        'password': parts[1].strip(),
        'policy': {
            'letter': policyParts[1],
            'minCount': int(quantParts[0]),
            'maxCount': int(quantParts[1])
        }   
    }

def is_valid_password(policy, password):
    letter_matches = 0
    for c in password:
        if c == policy['letter']:
            letter_matches += 1
    return policy['minCount'] <= letter_matches <= policy['maxCount']

with open('files/day2.txt', 'r') as f:
    lines = f.readlines()
    valid_passwords = 0
    for line in lines:
        parsed = parse_line(line)
        if is_valid_password(parsed['policy'], parsed['password']):
            valid_passwords += 1

print("There are {f} valid passwords".format(f=valid_passwords))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")