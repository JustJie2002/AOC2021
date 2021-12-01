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
            real = r.read().splitlines()
            real = [int(n) for n in real]
        return real

class Solution:
    def __init__(self, data):
        self.data = data

    def Part_One(self):
        ans = 0
        for i in range(1, len(self.data)):
            ans += self.data[i] > self.data[i - 1]
        return ans

    def Part_Two(self):
        m = [0 for _ in range(len(self.data))]
        for i in range(len(self.data) - 2):
            m[i] += self.data[i] + self.data[i + 1] + self.data[i + 2]
        ans = 0
        for i in range(1, len(self.data)):
            ans += m[i] > m[i - 1]
        return ans
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")