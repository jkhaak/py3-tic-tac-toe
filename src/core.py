#!/usr/bin/env python3

from .utils import concat, chop, drop_at, transpose
from .draw import show_board, cls, goto


def new_game():
    return Game.empty()


def get_input():
    try:
        return int(input())
    except ValueError:
        return None


def play():
    game = new_game()
    running = True
    while running:
        cls()
        goto(1, 1)
        game.draw_board()

        if game.wins():
            print("Player {} wins!".format(game.get_player()))
            running = False
        elif game.full():
            print("It is a draw!")
            running = False
        else:
            command = get_input()
            if command is None:
                print("Error: invalid input")
                continue
            else:
                game = game.move(command)


class Game:
    board_size = 3

    def __init__(self, player, grid):
        self.player = player
        self.grid = grid

    @classmethod
    def empty(cls):
        return Game(1, [0 for _ in range(cls.board_size ** 2)])

    def _str_player(self, i):
        if i == 1:
            return "O"
        elif i == 2:
            return "X"
        return " "

    def get_player(self):
        return self._str_player(self.player)

    def valid_move(self, i):
        return 1 <= i and i <= 9 and self.grid[i - 1] == 0

    def next_player(self):
        return 2 if self.player == 1 else 1

    def move(self, move):
        if not self.valid_move(move):
            return self

        init, tail = drop_at(move, self.grid)
        new_grid = init + [self.next_player()] + tail

        return Game(self.next_player(), new_grid)

    def draw_board(self):
        grid = chop(3, [self._str_player(i) for i in self.grid])
        show_board(grid)

    def wins(self):
        def diag(xs):
            return [xs[i][i] for i in range(0, 3)]

        # check: row, column, diagonal
        pl = self.player
        grid = chop(3, self.grid)
        rows = [[i == pl for i in row] for row in grid]
        cols = [[i == pl for i in col] for col in transpose(grid)]

        mirrored = [row[::-1] for row in grid]
        diags = [[i == pl for i in diag(grid)], [i == pl for i in diag(mirrored)]]

        return any([all(i) for i in rows + cols + diags])

    def full(self):
        return all([i != 0 for i in self.grid])
