# Conways Game of Life (Curses/Terminal)

*This project is an adaptation of Conway's Game of Life, forked from [Frazer Mill's Python Pygame version](https://github.com/frazermills/Conways-Game-of-life)

## Rules of the game:

* The game is operated on an infinite, two-dimensional, orthogonal grid of square cells.
* Each one of these cells have two states (alive or dead). The cells follow these rules:
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
