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
        self.dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.N = len(self.data[0])
        self.M = len(self.data)
        self.container = []

    def in_bound(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.M

    def consider(self, x, y):
        for dx, dy in self.dirs:
            if self.in_bound(x + dx, y + dy):
                if int(self.data[y + dy][x + dx]) <= int(self.data[y][x]):
                    return False
        return True

    def Part_One(self):
        ans = 0
        for y in range(self.M):
            for x in range(self.N):
                if self.consider(x, y):
                    self.container.append((y, x))
                    ans += int(self.data[y][x]) + 1
        return ans

    def Part_Two(self):
        counter = Counter()
        vis = [[False for _ in range(self.N)] for _ in range(self.M)]
        from queue import Queue
        q = Queue()
        for coordinate in self.container:
            q.put([coordinate, coordinate])
            vis[coordinate[0]][coordinate[1]] = True

        def in_bound(x, y):
            return 0 <= x < self.N and 0 <= y < self.M and self.data[y][x] != '9' and not vis[y][x]

        # 4-Directional BFS
        while not q.empty():
            father, cur = q.get()
            counter[father] += 1
            for dx, dy in self.dirs:
                if in_bound(cur[1] + dx, cur[0] + dy):
                    q.put([father, (cur[0] + dy, cur[1] + dx)])
                    vis[cur[0] + dy][cur[1] + dx] = True

        ans = 1
        for _, count in counter.most_common(3):
            ans *= count 
        return ans

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")