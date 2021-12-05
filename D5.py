from collections import *
from itertools import *
from functools import *
from heapq import *
from math import *
from copy import *
import bisect
import string

class Read:
    def Real(self):
        with open("input.txt", "a+") as r:
            r.seek(0)
            real = r.read().strip().splitlines()
        return real

class Solution:
    def __init__(self, data):
        self.data = [line.split(" -> ") for line in data]

    def Part_One(self):
        board = defaultdict(int)
        for start, end in self.data:
            x1, y1 = [int(x) for x in start.split(',')]
            x2, y2 = [int(x) for x in end.split(',')]
            if x1 == x2:
                board[(x1, y1)] += 1
                dy = (y2 - y1) / abs(y2 - y1)
                while y1 != y2:
                    y1 += dy
                    board[(x1, y1)] += 1

            elif y1 == y2:
                board[(x1, y1)] += 1
                dx = (x2 - x1) / abs(x2 - x1)
                while x1 != x2:
                    x1 += dx
                    board[(x1, y1)] += 1
        return sum(x >= 2 for x in board.values())

    def Part_Two(self):
        board = defaultdict(int)
        for start, end in self.data:
            x1, y1 = [int(x) for x in start.split(',')]
            x2, y2 = [int(x) for x in end.split(',')]
            board[(x1, y1)] += 1
            if x1 == x2:
                dy = (y2 - y1) / abs(y2 - y1)
                while y1 != y2:
                    y1 += dy
                    board[(x1, y1)] += 1

            elif y1 == y2:
                dx = (x2 - x1) / abs(x2 - x1)
                while x1 != x2:
                    x1 += dx
                    board[(x1, y1)] += 1
            
            else:
                dx = (x2 - x1) / abs(x2 - x1)
                dy = (y2 - y1) / abs(y2 - y1)
                while x1 != x2 and y1 != y2:
                    x1 += dx
                    y1 += dy
                    board[(x1, y1)] += 1
        return sum(x >= 2 for x in board.values())
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")