
from functools import reduce
from .utils import concat, zipWith, interleave

def cls():
    print(u'\033[2J')


def goto(x,y):
    print(u'\033[{};{}H'.format(y,x))


def show_player(player):
    return ['   ', ' {} '.format(player), '   ']


def show_row(row):
    bar = ['|' for _ in range(3)]
    besides = lambda xs,ys: zipWith(lambda x,y: x+y, xs, ys)
    return reduce(besides, interleave(bar, list(map(show_player, row))))


def show_board(grid):
    board_size = 3
    bar = ['-' * (board_size*4-1)]
    board = concat(interleave(bar, list(map(show_row, grid))))
    print('\n'.join(board))


