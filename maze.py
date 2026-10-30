import random
import time
from cell import Cell
from window import Window

class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        rows: int,
        cols: int,
        size_x: float,
        size_y: float,
        win: Window | None = None,
        seed: int | None = None,
    ):
        self.x1: int = x1
        self.y1: int = y1
        self.rows: int = rows
        self.cols: int = cols
        self.cell_size_x: float = size_x
        self.cell_size_y: float = size_y
        self.__win: Window = win
        if seed:
            random.seed(seed)
        self.__cells: list[list[Cell]] = [
            [Cell(self.__win) for i in range(self.cols)] for j in range(self.rows)
        ]
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_visited()

    def solve(self):
        return self.__solve_r(0, 0)

    def __create_cells(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.__draw_cell(x, y)

    def __draw_cell(self, row: int, col: int):
        x_pad = self.x1 + row * self.cell_size_x
        y_pad = self.y1 + col * self.cell_size_y
        if self.__win == None:
            return
        self.__cells[row][col].draw(
            x_pad, y_pad, x_pad + self.cell_size_x, y_pad + self.cell_size_y
        )
        self.__animate()

    def __animate(self, interval=0.01):
        self.__win.redraw()
        time.sleep(interval)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top = False
        self.__draw_cell(0, 0)
        self.__cells[self.rows - 1][self.cols - 1].has_bottom = False
        self.__draw_cell(self.rows - 1, self.cols - 1)

    def __break_walls_r(self, row, col, itter=0):
        self.__cells[row][col].visited = True
        while True:
            # time.sleep(1)
            to_visit = []
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                # Skip outliers
                if r < 0 or c < 0 or r >= self.rows or c >= self.cols:
                    continue
                if self.__cells[r][c].visited == False:
                    to_visit.append((r, c))
            if len(to_visit) == 0:
                # Redraw if window exists
                if self.__win:
                    self.__draw_cell(row, col)
                    self.__win.redraw()
                return
            next = random.choice(to_visit)
            # print(f"{next}, {itter}")
            # Selected cell is below current
            if next[0] > row:
                self.__cells[row][col].has_bottom = False
                self.__cells[next[0]][next[1]].has_top = False
            # Selected cell is atop current
            elif next[0] < row:
                self.__cells[row][col].has_top = False
                self.__cells[next[0]][next[1]].has_bottom = False
            # Selected cell is to the right of current
            elif next[1] > col:
                self.__cells[row][col].has_right = False
                self.__cells[next[0]][next[1]].has_left = False
            # Selected cell is to the left of current
            elif next[1] < col:
                self.__cells[row][col].has_left = False
                self.__cells[next[0]][next[1]].has_right = False

            # Redraw if window exists
            if self.__win:
                self.__draw_cell(row, col)
                self.__draw_cell(next[0], next[1])
                self.__win.redraw()
            # if itter >= 10: return
            self.__break_walls_r(next[0], next[1], itter + 1)

    def __solve_r(self, row, col):
        self.__animate()
        self.__cells[row][col].visited = True
        if row == self.rows - 1 and col == self.cols - 1:
            return True
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            # Skip outliers
            if r < 0 or c < 0 or r >= self.rows or c >= self.cols:
                continue
            # Make a move
            move = self.__determine_move(row, col, r, c)
            if move and not self.__cells[r][c].visited:
                self.__cells[row][col].draw_move(self.__cells[r][c])
                if self.__solve_r(r, c):
                    return True
                self.__cells[row][col].draw_move(self.__cells[r][c], True)
        return False

    def __determine_move(self, r1, c1, r2, c2):
        cell1:Cell = self.__cells[r1][c1]
        cell2:Cell = self.__cells[r2][c2]
        # cell 1 is above cell 2
        if r1 < r2:
            return not cell1.has_bottom
        # cell 1 is below cell 2
        if r1 > r2:
            return not cell1.has_top
        # cell 1 is to the left of cell 2
        if c1 < c2:
            return not cell1.has_right
        # cell 1 is to the right of cell 2
        if c1 > c2:
            return not cell1.has_left
        print("None found")
        return False

    def __reset_visited(self):
        for r in self.__cells:
            for c in r:
                c.visited = False
