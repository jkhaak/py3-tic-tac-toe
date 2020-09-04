# Tic-tac-toe


## Install

Requires python 3 and optionally pipenv

If using pipenv run `pipenv install` before playing


## Play

With pipenv just run `pipenv run app`.

With python run the `main.py` file.


## Development environment

Install required packages with `pipenv install`.

Enter ipython shell with `pipenv run ipython`.


Some tips for development. Because the Game object is immutable it opens a possibility to run and test code in ipython environment.

First start by importing all the necessary modules.

```ipython
In [1]: import tic_tac_toe.core as c

In [2]: import tic_tac_toe.draw as d

In [3]: import tic_tac_toe.utils as u
```

For example: to debug row printing one could do the following. First create a debugging function which mimics the `show_board` function. And then call it with some game state.

```ipython
In [4]: def draw(grid):
   ...:     bar = ["-" * (3 * 4 -1)]
   ...:     board = u.interleave(bar, [d.show_row(row) for row in grid])
   ...:     return board
   ...:

In [5]: c.Game.new_game().move(1).move(2).move(7).move(5).move(9).draw_board(draw)
Out[5]:
[['   |   |   ', ' X | O |   ', '   |   |   '],
 ['-----------'],
 ['   |   |   ', '   | O |   ', '   |   |   '],
 ['-----------'],
 ['   |   |   ', ' X |   | X ', '   |   |   ']]

In [6]: u.concat(c.Game.new_game().move(1).move(2).move(7).move(5).move(9).draw_board(draw))
Out[6]:
['   |   |   ',
 ' X | O |   ',
 '   |   |   ',
 '-----------',
 '   |   |   ',
 '   | O |   ',
 '   |   |   ',
 '-----------',
 '   |   |   ',
 ' X |   | X ',
 '   |   |   ']
```


## Generate documentation

Run `pipenv run gendoc` or by hand `python -m pydoc -w tic_tac_toe tic_tac_toe.core tic_tac_toe.draw tic_tac_toe.utils`

