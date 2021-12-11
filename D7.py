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
        self.data = sorted([int(x) for x in data])
        self.size = len(self.data)

    def Part_One(self):
        mid1 = self.size // 2
        mid2 = mid1 + 1
        cur1 = 0
        cur2 = 0
        for x in self.data:
            cur1 += abs(x - self.data[mid1])
            cur2 += abs(x - self.data[mid2])
        return min(cur1, cur2)

    def Part_Two(self):
        start = self.data[0]
        end = self.data[-1]
        ans = 10 ** 9
        for x in range(start, end + 1):
            cur = 0
            for v in self.data:
                diff = abs(v - x)
                cur += diff * (diff + 1) // 2
            ans = min(ans, cur)
        return ans
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")