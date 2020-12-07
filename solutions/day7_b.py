from utils import Timer
from utils import Vec2
from utils import pi
import math

DAY=7
PART='b'

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
                rules[color][" ".join(bParts[1:3])] = int(bParts[0])
    return rules

def calculate_sub_bags(color, rules):
    print (color)
    if color not in rules:
        print ("Not in rules")
        return 0
    else:
        sub_bags = 0

        for key in rules[color]:
            if key not in rules:
                print ("Plus " + str(rules[color][key]))
                sub_bags += rules[color][key]
            else:
                sub_total = calculate_sub_bags(key, rules)
                print ("Plus " + str(rules[color][key]) + " * " + str(sub_total))
                sub_bags += rules[color][key] + rules[color][key] * sub_total
    print(sub_bags)
    return sub_bags

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

print(rules)

result = calculate_sub_bags('shiny gold', rules)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")