#!/usr/bin/env python3

import functools
from .utils import concat, chop, drop_at
from .draw import show_board


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


def wins():
    pass


def full():
    pass


def play(grid, player):
    if wins():
        pass


def main():
    play(Game.empty())


if __name__ == '__main__':
    main()
