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
        self.data = data

    def Part_One(self):
        cnt = [[0, 0] for _ in range(len(self.data[0]))]
        for x in self.data:
            for i in range(len(x)):
                cnt[i][int(x[i])] += 1
        ans = ""
        res = ""
        for a, b in cnt:
            if a > b:
                ans += '0'
                res += '1'
            else:
                ans += '1'
                res += '0'
        return int(ans, 2) * int(res, 2)

    def consider(self, bits, index, switch):
        count = [0, 0]
        for bit in bits:
            if bit[index] == '1':
                count[1] += 1
            else:
                count[0] += 1
        
        win = "0-0"
        if switch:
            if count[1] >= count[0]:
                win = '1'
            else:
                win = '0'
        else:
            if count[0] <= count[1]:
                win = '0'
            else:
                win = '1'
        
        rets = []
        for bit in bits:
            if bit[index] == win:
                rets.append(bit)
        return rets

    def Part_Two(self):
        # Find Oxygen Generator Rating
        Bits = self.data[:]
        index = 0
        size = len(Bits[0])
        while len(Bits) != 1:
            Bits = self.consider(Bits, index, True)
            index = (index + 1) % size
            # print("Bits: {}".format(Bits))
        OGR = int(Bits[0], 2)

        # Find CO2 Scrubber Rating
        Bits = self.data[:]
        index = 0
        size = len(Bits[0])
        while len(Bits) != 1:
            Bits = self.consider(Bits, index, False)
            index = (index + 1) % size
            # print("Bits: {}".format(Bits))
        CSR = int(Bits[0], 2)
        return OGR * CSR
    
if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")