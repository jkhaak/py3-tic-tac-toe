import functools as ft
from .utils import concat, zip_with, interleave


def cls():
    """
    Clears the terminal view.
    """
    print(u"\033[2J")


def goto(x, y):
    """
    Move terminal cursor to specific point.
    """
    print(u"\033[{};{}H".format(y, x))


def show_player(player):
    """
    Returns a list of three elements which form one cell in the game view.
    """
    return ["   ", " {} ".format(player), "   "]


def show_row(row):
    """
    Creates a game row for later printing. Returns row in a list which each element represents a printable row in the game view.
    """
    cell_height = 3
    bar = ["|" for _ in range(cell_height)]
    besides = ft.partial(zip_with, lambda x, y: x + y)
    return ft.reduce(besides, interleave(bar, [show_player(p) for p in row]))


def show_board(grid):
    """
    Prints the whole board.

    Joins rows together with dashed lines before printing.
    """
    bar = ["-" * (len(grid) * 4 - 1)]
    board = concat(interleave(bar, [show_row(row) for row in grid]))
    print("\n".join(board))
