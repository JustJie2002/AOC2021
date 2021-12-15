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
        self.data = [s.split(' | ') for s in data]

    def Part_One(self):
        ans = 0
        unique = [2, 3, 4, 7]
        for digits, output in self.data:
            for word in output.split(' '):
                size = len(word)
                if size in unique:
                    ans += 1
        return ans

    def count_in(self, required, word):
        count = 0
        for char in required:
            if char in word:
                count += 1
        return count

    def consider(self, correspond):
        ans = [None for _ in range(10)]
        ans[7] = "".join(sorted(correspond[3][0]))
        ans[1] = "".join(sorted(correspond[2][0]))
        ans[4] = "".join(sorted(correspond[4][0]))
        ans[8] = "".join(sorted(correspond[7][0]))
        for i, word in enumerate(correspond[5]):
            if self.count_in(ans[7], word) == 3:
                ans[3] = "".join(sorted(word))
                correspond[5].pop(i)
                break

        for word in correspond[6]:
            if self.count_in(ans[4], word) == 4:
                ans[9] = "".join(sorted(word))
            elif self.count_in(ans[7], word) == 3:
                ans[0] = "".join(sorted(word))
            else:
                ans[6] = "".join(sorted(word))

        for word in correspond[5]:
            if self.count_in(ans[9], word) == 5:
                ans[5] = "".join(sorted(word))
            else:
                ans[2] = "".join(sorted(word))

        return ans

    def decide(self, corresponding_digits, words):
        ans = ""
        for word in words:
            ans += str(corresponding_digits.index("".join(sorted(word))))
        return int(ans)

    def Part_Two(self):
        output_values = 0
        for digits, output in self.data:
            correspond = defaultdict(list)
            for digit in digits.split(' '):
                size = len(digit)
                correspond[size].append(digit)
            corresponding_digits = self.consider(correspond)
            output_value = self.decide(corresponding_digits, output.split(' '))
            output_values += output_value
        return output_values
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")