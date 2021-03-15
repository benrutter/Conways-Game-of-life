import random
import curses
import time

class Grid:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = self.stdscr.getmaxyx()
        self.height -= 5
        self.width -= 5
        self.grid = self.create_random_grid(self.width, self.height)

    def create_random_grid(self, width, height):
        return [[random.choice([0,0,0,0,0,0,0,0,0,0,0,0,1]) for i in range(width)] for j in range(height)]

    def count_live_neighbours(self, y, x):

        left_x = x-1
        right_x = x+1
        below_y = y+1
        above_y = y-1
        if left_x < 0:
            left_x = self.width - 1
        elif right_x > self.width:
            right_x = 0
        if above_y < 0:
            above_y = self.height - 1
        elif below_y > self.height:
            below_y = 0

        neighbours = [
            self.grid[above_y][left_x],
            self.grid[above_y][x],
            self.grid[above_y][right_x],
            self.grid[y][right_x],
            self.grid[below_y][right_x],
            self.grid[below_y][x],
            self.grid[below_y][left_x],
            self.grid[y][left_x],
        ]

        live_neighbours = [n for n in neighbours if n == 1]
        return len(live_neighbours)


    def next_state(self, y, x):
        live_neighbours = self.count_live_neighbours(y, x)
        is_alive = self.grid[y][x] == 1
        if is_alive and live_neighbours == 2:
            return 1
        if live_neighbours == 3:
            return 1
        else:
            return 0

    def update(self):
        new_grid = self.grid.copy()
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                new_grid[y][x] = self.next_state(y, x)
        self.grid = new_grid

    def display(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                cell = self.grid[y][x]
                translate = {0:' ', 1:'▒'}
                self.stdscr.addch(y+2, x+3, translate[cell])
        self.stdscr.refresh()

def main(stdscr):
    grid = Grid(stdscr)
    while True:
        grid.display()
        grid.update()
        time.sleep(0.04)

if __name__ == '__main__':
    curses.wrapper(main)
