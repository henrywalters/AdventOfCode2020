from utils import Timer
from utils import Vec2
from utils import pi
import math
import regex

DAY=19
PART='b'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def get_regex_from_rules(rules, idx):
    def expand(word):
        return group(int(word)) if word.isdigit() else word
    def group(idx):
        return '(?:' + ''.join(map(expand, rules[idx].split())) + ')'

    regex = group(idx)
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
    rules[8] = '42 +'
    rules[11] = '(?P<group> 42 (?&group)? 31 )'

    reg = get_regex_from_rules(rules, 0)
    print (reg)
    reg = regex.compile(reg)

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