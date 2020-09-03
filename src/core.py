#!/usr/bin/env python3

import tty
import sys
import functools
from .utils import concat, chop, drop_at
from .draw import show_board, cls, goto


class Game():
    def __init__(self, player, grid):
        self.player = player
        self.grid = grid

    @classmethod
    def empty(cls):
        grid = chop(3, [0 for _ in range(9)])
        return Game(1, grid)

    def valid_move(self, i):
        return 1 <= i and i <= 9 and concat(self.grid)[i-1] == 0

    def next(self):
        return 2 if self.player == 1 else 1

    def move(self, move):
        if not self.valid_move(move):
            return self

        init, tail = drop_at(move, concat(self.grid))
        grid = chop(3, init + [self.player] + tail)

        return Game(self.next(), grid)

    def draw_board(self):
        show_board(self.grid)

    def wins(self):
        pass

    def full(self):
        pass

    def play(self):
        while True:
            cls()
            goto(1,1)
            show_board(self.grid)

