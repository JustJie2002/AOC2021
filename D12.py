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
        self.data = [relation.split('-') for relation in data]
        self.adj = defaultdict(list)
        for u, v in self.data:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.vis = set()
        self.goal = "end"
        self.path = set()
        self.entered = Counter()

    def dfs(self, curr, path = "start"):
        for v in self.adj[curr]:
            if v == self.goal:
                self.path.add(path)
                continue
            if v == "start":
                continue
            if v not in self.vis:
                if v.islower():
                    self.vis.add(v)
                self.dfs(v, path + ', ' + v)
                if v in self.vis:
                    self.vis.remove(v)

    def Part_One(self):
        # DFS
        self.dfs("start")
        return len(self.path)

    def Part_Two(self):
        # BFS
        from queue import Queue as queue
        start = ("start", set(["start"]), None)
        ans = 0
        q = queue()
        q.put(start)
        while not q.empty():
            cur, path, twice = q.get()
            if cur == self.goal:
                ans += 1
                continue
            for v in self.adj[cur]:
                if v not in path:
                    new_path = set(path)
                    if v.islower():
                        new_path.add(v)
                    q.put((v, new_path, twice))
                elif v in path and twice is None and v not in ["start", "end"]:
                    q.put((v, path, v))
        return ans

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")