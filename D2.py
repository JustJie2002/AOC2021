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
        return real

class Solution:
    def __init__(self, data):
        self.data = data

    def Part_One(self):
        hort = 0
        depth = 0
        for x in self.data:
            direction, e = x.split()
            if direction == "forward":
                hort += int(e)
            elif direction == "down":
                depth += int(e)
            elif direction == "up":
                depth -= int(e)
        return hort * depth

    def Part_Two(self):
        aim = 0
        hort = 0
        depth = 0
        for x in self.data:
            direction, e = x.split()
            if direction == "up":
                aim -= int(e)
            elif direction == "down":
                aim += int(e)
            elif direction == "forward":
                hort += int(e)
                depth += int(e) * aim
            # print(aim, hort, depth)
        return hort * depth

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")