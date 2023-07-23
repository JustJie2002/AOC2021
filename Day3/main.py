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
            for line in raw_data.splitlines():
                data.append(line)
        return data

class Solver:
    def __init__(self, data):
        self.data = data

    def Part_One(self):
        n = len(self.data[0])

        freq = [Counter() for _ in range(n)]
        for binary in self.data:
            for i in range(n):
                freq[i][binary[i]] += 1
        
        gam = eps = ""
        for i in range(n):
            gam += freq[i].most_common()[0][0]
            eps += freq[i].most_common()[1][0]

        a = int(gam, 2)
        b = int(eps, 2)

        return a * b

    def Part_Two(self):
        m = len(self.data[0])

        res = self.data[:]
        ptr = 0
        while len(res) != 1:
            freq = Counter(b[ptr] for b in res)
            det = '1'
            if freq['0'] > freq['1']:
                det = '0'
            next_res = []
            for b in res:
                if b[ptr] == det:
                    next_res.append(b)
            res = next_res
            ptr = (ptr + 1) % m
        oxy = int(res[0], 2)

        res = self.data[:]
        ptr = 0
        while len(res) != 1:
            freq = Counter(b[ptr] for b in res)
            det = '0'
            if freq['1'] < freq['0']:
                det = '1'
            next_res = []
            for b in res:
                if b[ptr] == det:
                    next_res.append(b)
            res = next_res
            ptr = (ptr + 1) % m
        co2 = int(res[0], 2)

        return oxy * co2
        


if __name__ == "__main__":
    reader = Reader("input.txt")
    data = reader.read()
    solver = Solver(data)
    print(f"The answer to Part One is {solver.Part_One()}")
    print(f"The answer to Part Two is {solver.Part_Two()}")