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
        self.left = ['(', '[', '{', '<']
        self.right = [')', ']', '}', '>']

    def Part_One(self):
        ans = 0
        points = {
          ')' : 3,
          ']' : 57,
          '}' : 1197,
          '>' : 25137
        }
        for line in self.data:
            stack = []
            for c in line:
                if c in self.right:
                    if not stack:
                        ans += points[c]
                        break
                    else:
                        opening = self.left.index(stack[-1])
                        closing = self.right.index(c)
                        if opening == closing:
                            stack.pop()
                        else:
                            ans += points[c]
                            break
                else:
                    stack.append(c)
        return ans

    def Part_Two(self):
        ans = 0
        points = {
          '(' : 1,
          '[' : 2,
          '{' : 3,
          '<' : 4
        }
        container = []

        def consider(st):
            nonlocal container
            st.reverse()
            need = 0
            for c in st:
                need *= 5
                need += points[c]
            container.append(need)

        for line in self.data:
            stack = []
            for c in line:
                bad = False
                if c in self.right:
                    if not stack:
                        bad = True
                        break
                    else:
                        opening = self.left.index(stack[-1])
                        closing = self.right.index(c)
                        if opening == closing:
                            stack.pop()
                        else:
                            bad = True
                            break
                else:
                    stack.append(c)
            if not bad:
                consider(stack)
        container.sort()
        return container[len(container) // 2]
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")