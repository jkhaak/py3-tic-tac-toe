#!/usr/bin/env python3

import functools
from .utils import concat, chop, drop_at
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
    while True:
        cls()
        goto(1,1)
        game.draw_board()

        if game.wins():
            print("Player {} wins!".format(game.get_player()))
        elif game.full():
            print("It is a draw!")
            input("Press enter to start a new game.")
            game = new_game()
        else:
            command = get_input()
            if command is None:
                print("Error: invalid input")
                continue
            else:
                game = game.move(command)



class Game():
    def __init__(self, player, grid):
        self.player = player
        self.grid = grid

    @classmethod
    def empty(cls):
        grid = chop(3, [0 for _ in range(9)])
        return Game(1, grid)

    def get_player(self):
        return 'O' if self.player == 1 else 'X'

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
        return False

    def full(self):
        return all([i != 0 for i in concat(self.grid)])

