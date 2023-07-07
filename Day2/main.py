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
            raw_data = fp.read()
            # TODO
        return data

class Solver:
    def __init__(self, data):
        self.data = data

    def Part_One(self):
        return "TBD"

    def Part_Two(self):
        return "TBD"
    

if __name__ == "__main__":
    reader = Reader("input.txt")
    data = reader.read()
    solver = Solver(data)
    print(f"The answer to Part One is {solver.Part_One()}")
    print(f"The answer to Part Two is {solver.Part_Two()}")