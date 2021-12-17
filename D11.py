from collections import *
from itertools import *
from functools import *
from heapq import *
from math import *
from copy import *
import bisect
import string
import pprint as pp

class Read:
    def Real(self):
        with open("input.txt", "a+") as r:
            r.seek(0)
            real = r.read().strip().splitlines()
        return real

class Grid:
    def __init__(self, data):
        self.backup = [[int(x) for x in line] for line in data]
        self.Grid = [[int(x) for x in line] for line in data]
        self.Directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        self.N = len(self.Grid)
        self.M = len(self.Grid[0])
        self.AllFlash = [[0 for _ in range(self.M)] for _ in range(self.N)]
        self.flash = 0
        self.used = [[False for _ in range(self.M)] for _ in range(self.N)]

    def in_bound(self, x, y):
        return 0 <= x < self.M and 0 <= y < self.N

    def simulate(self, x, y):
        self.flash += 1
        self.used[y][x] = True
        for dx, dy in self.Directions:
            new_x = x + dx
            new_y = y + dy
            if self.in_bound(new_x, new_y) and not self.used[new_y][new_x]:
                self.Grid[new_y][new_x] += 1
                if self.Grid[new_y][new_x] >= 10:
                    self.simulate(new_x, new_y)

    def reset(self):
        self.used = [[False for _ in range(self.M)] for _ in range(self.N)]

    def global_reset(self):
        self.Grid = self.backup

    def change(self):
        for y in range(self.N):
            for x in range(self.M):
                self.Grid[y][x] += 1
                if self.Grid[y][x] >= 10 and not self.used[y][x]:
                    self.simulate(x, y)
        for y in range(self.N):
            for x in range(self.M):
                if self.used[y][x] == True:
                    self.Grid[y][x] = 0
        # pp.pprint(self.Grid)
        self.reset()

    def check(self):
        return self.Grid == self.AllFlash

class Solution:
    def __init__(self, data):
        self.data = Grid(data)
        
    def Part_One(self):
        for _ in range(100):
            self.data.change()
        return self.data.flash

    def Part_Two(self):
        self.data.global_reset()
        step = 1
        while True:
            self.data.change()
            if self.data.check():
                break
            step += 1
        return step
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")