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
            for x in raw_data:
                x = int(x)
                data.append(x)
        return data

class Solver:
    def __init__(self, data):
        self.data = data
        self.n = len(self.data)

    def Part_One(self):
        res = 0
        for i in range(1, self.n):
            if self.data[i] > self.data[i - 1]:
                res += 1
        return res

    def Part_Two(self):
        pre = [0] * (self.n + 1)
        for i in range(self.n):
            pre[i + 1] = pre[i] + self.data[i]
        def get(i):
            return pre[i + 1] - pre[i - 2]
        res = 0
        for i in range(3, self.n):
            if get(i) > get(i - 1):
                res += 1
        return res

if __name__ == "__main__":
    reader = Reader("input.txt")
    data = reader.read()
    solver = Solver(data)
    print(f"The answer to Part One is {solver.Part_One()}")
    print(f"The answer to Part Two is {solver.Part_Two()}")