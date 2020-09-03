from src.core import new_game
from src.draw import cls, goto


def play(game):
    while True:
        cls()
        goto(1,1)
        game.draw_board()
        command = input()



if __name__ == '__main__':
    try:
        play(new_game())
    except KeyboardInterrupt:
        pass

