import time

class Timer:
    def __init__(self):
        self.start = time.perf_counter()

    def start(self):
        self.start = time.perf_counter()

    def stop(self):
        return time.perf_counter() - self.start
        

def xor(a, b):
    return (a or b) and not (a and b)