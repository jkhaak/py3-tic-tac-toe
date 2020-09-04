#!/usr/bin/env python3

from .utils import concat, chop, drop_at, transpose
from .draw import show_board, cls, goto


def get_input(msg=""):
    try:
        return int(input(msg))
    except ValueError:
        return None


def play():
    game = Game.new_game()
    instructions = "Player {} choose a cell with numbers 1-9: "

    while True:
        cls()
        goto(1, 1)
        game.draw_board()

        if game.wins():
            print("Player {} wins!".format(game.winner()))
            break
        elif game.full():
            print("It is a draw!")
            break

        command = get_input(instructions.format(game.get_player()))
        if command is not None:
            game = game.move(command)


class Game:
    board_size = 3

    def __init__(self, player, grid):
        self.player = player
        self.grid = grid

    @classmethod
    def new_game(cls):
        return Game(1, chop(3, [0 for _ in range(cls.board_size ** 2)]))

    def _str_player(self, i):
        if i == 1:
            return "O"
        elif i == 2:
            return "X"
        return " "

    def winner(self):
        return self._str_player(self.player)

    def get_player(self):
        return self._str_player(self.next_player())

    def valid_move(self, i):
        return 1 <= i and i <= 9 and concat(self.grid)[i - 1] == 0

    def next_player(self):
        return 2 if self.player == 1 else 1

    def move(self, move):
        if not self.valid_move(move):
            return self

        init, tail = drop_at(move, concat(self.grid))
        new_grid = init + [self.next_player()] + tail

        return Game(self.next_player(), chop(3, new_grid))

    def draw_board(self):
        show_board([[self._str_player(p) for p in row] for row in self.grid])

    def wins(self):
        def diag(xs):
            return [xs[i][i] for i in range(0, 3)]

        # check: row, column, diagonal
        pl = self.player
        rows = [[i == pl for i in row] for row in self.grid]
        cols = [[i == pl for i in col] for col in transpose(self.grid)]

        mirrored = [row[::-1] for row in self.grid]
        diags = [[i == pl for i in diag(self.grid)], [i == pl for i in diag(mirrored)]]

        return any([all(i) for i in rows + cols + diags])

    def full(self):
        return all([i != 0 for row in self.grid for i in row])
