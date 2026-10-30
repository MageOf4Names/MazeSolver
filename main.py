from window import Window
from maze import Maze

def main():
    pad = 10
    size = 50
    rows = 20
    cols = 20
    win = Window(cols * size + 2 * pad, rows * size + 2 * pad)
    maze = Maze(pad, pad, rows, cols, size, size, win, 10)
    print(maze.solve())
    win.wait_for_close()

if __name__ == "__main__":
    main()
