from collections import *
from itertools import *
from functools import *
from heapq import *
from math import *
from copy import *
import bisect
import string

class Reader:
    def __init__(self, fname):
        self.fname = fname

    def read(self):
        data = []
        with open(self.fname, "r") as fp:
            raw_data = fp.read().splitlines()
            for d in raw_data:
                op, x = d.split()
                x = int(x)
                data.append((op, x))
        return data

class Solver:
    def __init__(self, data):
        self.data = data

    def Part_One(self):
        xDir, dep = 0, 0
        for op, x in self.data:
            if op == "forward":
                xDir += x
            elif op == "down":
                dep += x
            elif op == "up":
                dep -= x
            else: assert False
        return xDir * dep

    def Part_Two(self):
        xDir, aim, dep = 0, 0, 0
        for op, x in self.data:
            if op == "forward":
                xDir += x
                dep += aim * x
            elif op == "down":
                aim += x
            elif op == "up":
                aim -= x
            else: assert False
        return xDir * dep
    

if __name__ == "__main__":
    reader = Reader("input.txt")
    data = reader.read()
    solver = Solver(data)
    print(f"The answer to Part One is {solver.Part_One()}")
    print(f"The answer to Part Two is {solver.Part_Two()}")