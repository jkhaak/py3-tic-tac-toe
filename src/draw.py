
import functools
from .utils import concat, zipWith, interleave

def show_player(player):
    middle = '   '
    if player == 1:
        middle = ' O '
    elif player == 2:
        middle = ' X '
    return ['   ', middle, '   ']


def show_row(row):
    bar = ['|' for _ in range(3)]
    besides = lambda xs,ys: zipWith(lambda x,y: x+y, xs, ys)
    return functools.reduce(besides, interleave(bar, list(map(show_player, row))))


def show_board(grid):
    board_size = 3
    bar = ['-' * (board_size*4-1)]
    board = concat(interleave(bar, list(map(show_row, grid))))
    print("\n".join(board))


