import random
import curses

class Grid:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.rows, self.cols = self.stdscr.getmaxyx()
        self.rows -= 1
        self.cols -= 1
        self.size = (self.rows, self.cols)
        self.arr = [[None for i in range(self.cols)] for i in range(self.rows)]

    def make_2d_array(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.arr[row][col] = random.randrange(2)

    def count_neighbours(self, row, col):
        neighbour_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                row_edge = (row + i + self.rows) % self.rows
                col_edge = (col + j + self.cols) % self.cols
                neighbour_sum += self.arr[row_edge][col_edge]

        neighbour_sum -= self.arr[row][col]
        return neighbour_sum

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.arr[row][col]
                translate = {0:' ', 1:'█'}
                self.stdscr.addch(row, col, translate[cell])
        self.stdscr.refresh()

    def update(self):
        nextArr = [[None for i in range(self.cols)] for i in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                state = self.arr[row][col]
                neighbours = self.count_neighbours(row, col)
                if state == 0 and neighbours == 3:
                    nextArr[row][col] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    nextArr[row][col] = 0
                else:
                    nextArr[row][col] = state

        self.arr = nextArr
