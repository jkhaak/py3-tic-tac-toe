from functools import reduce, partial
from .utils import concat, zip_with, interleave


def cls():
    print(u"\033[2J")


def goto(x, y):
    print(u"\033[{};{}H".format(y, x))


def show_player(player):
    return ["   ", " {} ".format(player), "   "]


def show_row(row, row_size=3):
    bar = ["|" for _ in range(row_size)]
    besides = partial(zip_with, lambda x, y: x + y)
    return reduce(besides, interleave(bar, [show_player(p) for p in row]))


def show_board(grid, board_size=3):
    bar = ["-" * (board_size * 4 - 1)]
    board = concat(interleave(bar, [show_row(row) for row in grid]))
    print("\n".join(board))
