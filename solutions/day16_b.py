from utils import Timer
from utils import Vec2
from utils import pi
from utils import Range
import math

DAY=16
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

rules = {}
rule_idx = {}
nearby_tickets = []
valid_tickets = []
scan_errors = []
my_ticket = []

own_ticket = []

def parse_notes():
    parsing_rules = True
    parsing_ticket = False
    parsing_nearby_tickets = False

    for l in lines:
        if l == '':
            continue
        elif l.strip() == 'your ticket:':
            print ("Parsing my ticket")
            parsing_ticket = True
        elif l == 'nearby tickets:':
            parsing_nearby_tickets = True
        elif parsing_nearby_tickets:
            nearby_tickets.append([int(x) for x in l.split(',')])
        elif parsing_ticket:
            my_ticket.append([int(x) for x in l.split(',')])

        else:
            parts = l.split(': ')
            ranges = parts[1].split(' or ')
            rA = ranges[0].split('-')
            rB = ranges[1].split('-')
            rules[parts[0]] = (
                Range(int(rA[0]), int(rA[1])),
                Range(int(rB[0]), int(rB[1]))
            )


def is_valid_ticket(ticket):
    valid_ticket = True
    for field in ticket:
        valid_field = False
        for rule in rules:
            if rules[rule][0].contains(field) or rules[rule][1].contains(field):
                valid_field = True
                break
        if not valid_field:
            scan_errors.append(field)
            valid_ticket = False

    if valid_ticket:
        valid_tickets.append(ticket)
    
    return valid_ticket


# basically like a suduko solver. start by working finding rows that only have 1 possible 
# idx then narrow down the results from there.
def parse_rule_idx():
    rc = len(rules)
    found = []
    while len(found) < rc:
        
        for rule in rules:
            rule_matches = []
            for i in range(len(valid_tickets[0])):
                idx_matches_rule = True
                for ticket in valid_tickets:
                    if not rules[rule][0].contains(ticket[i]) and not rules[rule][1].contains(ticket[i]):
                        idx_matches_rule = False
                        break
                
                if idx_matches_rule:
                    rule_matches.append((rule, i))

            unfound_matches = []
            for match in rule_matches:
                if match[1] not in found:
                    unfound_matches.append(match)
            if len(unfound_matches) == 1:
                rule_idx[rule] = unfound_matches[0][1]
                found.append(unfound_matches[0][1])


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

parse_notes()

for ticket in nearby_tickets:
    is_valid_ticket(ticket)

parse_rule_idx()

print (rule_idx)

result = 1

print (my_ticket)

for rule in rules:
    if 'departure' in rule:
        result *= my_ticket[0][rule_idx[rule]]

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")