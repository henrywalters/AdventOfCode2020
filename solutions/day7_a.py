from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=7
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

result = 0

def parse_rules(lines):
    rules = {}
    for line in lines:
        color = " ".join(line.split(' ')[0:2])
        contents = line.split('bags contain ')[1]
        if contents != 'no other bags.':
            rules[color] = {}
            bags = contents.split(', ')
            for bag in bags:
                bParts = bag.split(' ')
                rules[color][" ".join(bParts[1:3])] = bParts[0]
    return rules

def rule_makes_color(rule, color, rules):
    print (rule, color)
    if rule == color:
        print("Match!")
        return True
    else:
        if rule in rules:
            for key in rules[rule]:
                if rule_makes_color(key, color, rules):
                    return True
    return False


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

rules = parse_rules(lines)

results = [rule_makes_color(rule, 'shiny gold', rules) for rule in rules]
result = sum([1 if r else 0 for r in results]) - 1
print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")