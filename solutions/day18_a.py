from utils import Timer
from utils import Vec2
from utils import pi
import math
import re

DAY=18
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def parse_expr(expr):

    prec = {
        '+': 1,
        '*': 0,
    }

    # Output Queue
    opq = []
    # Operator stack
    os = []

    ## Generate RPN
    for i in range(len(expr)):
        if re.match(r'\d{1}', expr[i]):
            opq.append(int(expr[i]))
        elif re.match(r'[*+]', expr[i]):
            op = expr[i]
            while len(os) > 0 and os[-1] != '(':
                opq.append(os.pop())
            os.append(op)
        elif expr[i] == '(':
            os.append(expr[i])
        elif expr[i] == ')':
            while len(os) > 0 and os[-1] != '(':
                opq.append(os.pop())
            if len(os) > 0 and os[-1] == '(':
                os.pop()

    while len(os) > 0:
        opq.append(os.pop())

    os = []

    for i in range(len(opq)):
        if type(opq[i]) == int:
            os.append(opq[i])
        elif opq[i] == '+':
            a = os.pop()
            b = os.pop()
            os.append(a + b)
        elif opq[i] == '*':
            a = os.pop()
            b = os.pop()
            os.append(a * b)
            
    return os.pop()


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

print(lines)

result = sum([parse_expr(l) for l in lines])

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")