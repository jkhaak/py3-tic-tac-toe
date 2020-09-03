from src.core import Game

if __name__ == '__main__':
    try:
        Game.empty().play()
    except KeyboardInterrupt:
        pass
