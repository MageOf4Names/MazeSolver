from tkinter import Tk, Canvas
from line import Line

class Window():

    def __init__(self, width: int, height: int):
        self.root = Tk()
        self.root.title("New Window")
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.runnning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
