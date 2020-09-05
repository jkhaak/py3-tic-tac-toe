#!/usr/bin/env python3

from .utils import concat, chop, drop_at, transpose
from .draw import show_board, cls, goto


def get_int_input(msg=""):
    """
    Helper function to query for integer input from the user.

    Returns None if user inputs incorrect value.
    """
    try:
        return int(input(msg))
    except ValueError:
        return None


def play():
    """
    Main game loop.

    Initialises game object. Checks for winning or draw conditions and asks for user input.
    """
    game = Game.new_game()
    instructions = "Player {} choose a cell with numbers 1-9: "

    while True:
        cls()
        goto(1, 1)
        game.draw_board(show_board)

        if game.wins():
            print("Player {} wins!".format(game.get_current_player()))
            break
        elif game.full():
            print("It is a draw!")
            break

        command = get_int_input(instructions.format(game.get_next_player()))
        if command is not None:
            game = game.move(command)


class Game:
    """
    Instance of this class contains the current state of the game and helper functions to inspect the game state.

    Construct a new empty game with new_game function.

    Move function will advance game state by returning a new state.
    """

    board_size = 3

    def __init__(self, player, grid):
        """
        Constructs a new game state from the given parameters.
        """
        self.player = player
        self.grid = grid

    @classmethod
    def new_game(cls):
        """
        Creates a blank game state. Used for initializing the game.
        """
        return Game(1, chop(3, [0 for _ in range(cls.board_size ** 2)]))

    def _str_player(self, i):
        """
        Helper function for changing internal data representation to printable format.
        """
        if i == 1:
            return "O"
        elif i == 2:
            return "X"
        return " "

    def get_current_player(self):
        """
        Return the avatar of the winning player. Either 'X' or 'O'.
        """
        return self._str_player(self.player)

    def get_next_player(self):
        """
        Return the avatar of the next player. Either 'X' or 'O'.
        """
        return self._str_player(self.next_player())

    def valid_move(self, i):
        """
        Checks if the guven move is valid.

        Return boolean. True for valid, False for invalid move.
        """
        return 1 <= i and i <= 9 and concat(self.grid)[i - 1] == 0

    def next_player(self):
        """
        Return the next player.
        """
        return 2 if self.player == 1 else 1

    def move(self, move):
        """
        Records the given move. First checks for validity and then returns the updated game object.
        """
        if not self.valid_move(move):
            return self

        init, tail = drop_at(move, concat(self.grid))
        new_grid = init + [self.next_player()] + tail

        return Game(self.next_player(), chop(3, new_grid))

    def draw_board(self, draw):
        """
        Calls given drawing function by giving the current data structure of the game to it.

        Return the result of draw function.
        """
        return draw([[self._str_player(p) for p in row] for row in self.grid])

    def wins(self):
        """
        Check for winning condition.

        Returns True if current player has won the game, otherwise False.
        """

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
        """
        Checks if the board is full.

        Return True if there are no more empty space available, otherwise False.
        """
        return all([i != 0 for row in self.grid for i in row])
