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


def pi(vals):
    val = 1
    for i in vals:
        val *= i
    return val


def xor(a, b):
    return (a or b) and not (a and b)

