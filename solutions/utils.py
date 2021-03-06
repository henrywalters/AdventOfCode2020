import time
import math

def deg2rad(deg):
    return deg * math.pi / 180

def min_tuple_list(tuples):
    m = None
    for t in tuples:
        if m is None or t[0] < m[0]:
            m = t
    return m


def print_list(L):
    for l in L:
        print(l)


def print_dict(D):
    for k in D:
        print("{k} = {v}".format(k=k, v=D[k]))


class Range:
    def __init__(self, m, M):
        self.min = m
        self.max = M

    def contains(self, val):
        return self.min <= val <= self.max

    def get_list(self):
        l = []
        for i in range(self.min, self.max + 1):
            l.append(i)
        return l

    def __str__(self):
        return '[{m}, {M}]'.format(m=self.min, M=self.max)


def chinese_remainder_theorem(items):
    """each item is a tuple, idx 0 = a and idx 1 = ni"""
    N = pi([x[1] for x in items])
    Y = [int(N / n[1]) for n in items]
    Z = [mul_inv(Y[i], items[i][1])  for i in range(len(items))]
    print(N)
    print(Z)
    print(Y)
    print(items)
    x = [Z[i] * Y[i] * items[i][0] for i in range(len(items))]
    print(x)
    return sum(x) % N

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


class Timer:
    def __init__(self):
        self.start = time.perf_counter()

    def start(self):
        self.start = time.perf_counter()

    def stop(self):
        return time.perf_counter() - self.start
        

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def add(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, deg):
        print(deg)
        x = math.cos(deg) * self.x - math.sin(deg) * self.y
        y = math.sin(deg) * self.x + math.cos(deg) * self.y
        self.x = x
        self.y =y

    def get_tuple(self):
        return (self.x, self.y)

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return "[{x}, {y}]".format(x=self.x, y=self.y)

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

def get_distribution(values):
    dist = {}
    for x in values:
        if x not in dist:
            dist[x] = 0
        dist[x] += 1
    return dist

def pi(vals):
    val = 1
    for i in vals:
        val *= i
    return val


def xor(a, b):
    return (a or b) and not (a and b)

def clamp(val, m, M):
    if val < m:
        return m
    elif val > M:
        return M
    else:
        return val

def in_bounds(arr, i, j):
    return i >= 0 and j >= 0 and i < len(arr) and j < len(arr[0])

def fibb_numbers(n):
    output = [1, 1]
    for i in range(2, n):
        output.append(output[i - 1] + output[i - 2])
    return output

def fibb(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        mem = {}
        mem[0] = 1
        mem[1] = 1
        output = 0
        for i in range(2, n):
            output = mem[i - 1] + mem[i - 2]
            mem[i] = output

        return output


def fibb_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibb_recursive(n - 1) + fibb_recursive(n - 2)


def time_fn(name, fn):
    timer = Timer()
    fn()
    print("{name} executed in {t} seconds".format(
        name=name,
        t=timer.stop()
    ))