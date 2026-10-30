from point import Point
from tkinter import Canvas

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.start = p1
        self.end = p2

    def draw(self, canvas: Canvas, color):
        canvas.create_line(
            self.start.y, self.start.x, self.end.y, self.end.x, fill=color, width=2
        )
