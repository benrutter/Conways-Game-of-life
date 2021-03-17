import grid
from curses import wrapper, curs_set
from time import sleep

def main(stdscr):
    curs_set(0)
    game_grid = grid.Grid(stdscr)
    game_grid.make_2d_array()

    while True:
        game_grid.display()
        game_grid.update()
        sleep(0.025)

if __name__ == "__main__":
    wrapper(main)
