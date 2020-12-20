from utils import Timer
from utils import Vec2
from utils import pi
import math
import re

DAY=19
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def get_regex_from_rules(rules):
    def expand(word):
        return group(int(word)) if word.isdigit() else word
    def group(idx):
        return '(?:' + ''.join(map(expand, rules[idx].split())) + ')'

    regex = group(0)
    print(regex)
    return regex


def parse_lines():
    rules = {}
    messages = []

    parsing_rules = True

    for l in lines:
        if l == '':
            parsing_rules = False
            continue
        if parsing_rules:
            idx, rule = l.rstrip().split(': ')
            rules[int(idx)] = rule.replace('"', '')
        else:
            messages.append(l)

    print(rules)

    regex = get_regex_from_rules(rules)
    reg = re.compile(regex)

    matches = []

    for msg in messages:
        print (msg)
        if reg.fullmatch(msg):
            matches.append(msg)

    print(matches)

    return matches


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    
result = len(parse_lines())

print ("Result = {result}".format(result=result))

# And stop here


execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")