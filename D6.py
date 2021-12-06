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
            real = r.read().strip().split(',')
        return real

class Solution:
    def __init__(self, data):
        self.data = [int(x) for x in data]

    def Part_One(self):
        # Brute Force
        stat = deepcopy(self.data)
        
        def simulate():
            nonlocal stat
            N = len(stat)
            new = []
            other = 0
            for i in range(N):
                curr = stat[i] - 1
                if curr == -1:
                    new.append(6)
                    other += 1
                else:
                    new.append(curr)
            new += [8] * other
            stat = new
        for _ in range(80):
            simulate()
        return len(stat)

    def Part_Two(self):
        counter = [0] * 9
        for day_remaining in self.data:
            counter[day_remaining] += 1
        for _ in range(256):
            counter = counter[1:7] + [counter[0] + counter[7], counter[8], counter[0]]
        return sum(counter)
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")