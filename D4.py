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
            real = r.read().strip().split("\n\n")
        return real

class Solution:
    def __init__(self, data):
        self.numbers = [int(x) for x in data[0].split(',')]
        self.boards = [[[int(x) for x in row.strip().split()] for row in board.split('\n')] for board in data[1:]]
        self.won = ['O', 'O', 'O', 'O', 'O']

    def check_win(self, board, index, r, c):
        # check valid
        if r == None or c == None:
            return None

        # check row
        row = board[r]
        if row == self.won:
            return self.boards[index][r]
        
        # check col
        col = [board[i][c] for i in range(5)]
        if col == self.won:
            return [self.boards[index][i][c] for i in range(5)]
        
        # if both row and col are won
        return None

    def simulate(self, board, choosen):
        for r in range(5):
            for c in range(5):
                if board[r][c] == choosen:
                    board[r][c] = 'O'
                    return r, c
        return None, None

    def Part_One(self):
        boards = deepcopy(self.boards)
        for x in self.numbers:
            for index, board in enumerate(boards):
                r, c = self.simulate(board, x)
                winning_board = self.check_win(board, index, r, c)
                if winning_board != None:
                    unmarked = 0
                    for i in range(5):
                        for j in range(5):
                            unmarked += (self.boards[index][i][j] if board[i][j] != 'O' else 0)
                    return unmarked * x


    def Part_Two(self):
        boards = deepcopy(self.boards)
        last = 0
        count = len(boards)
        distinct = set()
        for x in self.numbers:
            for index, board in enumerate(boards):
                r, c = self.simulate(board, x)
                winning_board = self.check_win(board, index, r, c)
                if winning_board != None:
                    distinct.add(index)
                    unmarked = 0
                    for i in range(5):
                        for j in range(5):
                            unmarked += (self.boards[index][i][j] if board[i][j] != 'O' else 0)
                    if len(distinct) == count:
                        return unmarked * x
    

if __name__ == "__main__":
    Real = Read().Real()
    Initialize = Solution(Real)
    print(f"The answer to Part One is {Initialize.Part_One()}")
    print(f"The answer to Part Two is {Initialize.Part_Two()}")