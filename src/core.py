#!/usr/bin/env python3

import functools


def concat(xss):
    return functools.reduce(lambda xs,ys: xs+ys, xss)


def chop(n, xs):
    if len(xs) == 0:
        return []
    return [xs[:n]] + chop(n, xs[n:])


def drop_at(i, xs):
    return xs[:i-1], xs[i:]


def show_player(player):
    middle = '   '
    if player == 1:
        middle = ' O '
    elif player == 2:
        middle = ' X '
    return ['   ', middle, '   ']


def zipWith(fn, xs, ys):
    return [fn(a,b) for (a,b) in zip(xs,ys)]


def interleave(x, xs):
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return xs
    return [xs[0]] + [x] + interleave(x, xs[1:])


def show_row(row):
    bar = ['|' for _ in range(3)]
    besides = lambda xs,ys: zipWith(lambda x,y: x+y, xs, ys)
    return functools.reduce(besides, interleave(bar, list(map(show_player, row))))


def draw_board(grid):
    board_size = 3
    bar = '-' * (board_size*4-1)
    print("\n".join(concat(interleave([bar], list(map(show_row, grid))))))


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
        draw_board(self.grid)


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
