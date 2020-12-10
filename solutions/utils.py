import time

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