from line import Line
from point import Point
from window import Window

class Cell():
    def __init__(self, win: Window | None = None):
        self.has_left:bool = True
        self.has_right:bool = True
        self.has_top:bool = True
        self.has_bottom:bool = True
        self.visited:bool = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y1 = -1
        self.__win = win

    def find_center(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win == None:
            return
        if self.has_top:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), 
                                      Point(self.__x1, self.__y2)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), 
                                      Point(self.__x1, self.__y2)), "light gray",)
        if self.has_right:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), 
                                      Point(self.__x2, self.__y2)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), 
                                      Point(self.__x2, self.__y2)), "light gray",)
        if self.has_bottom:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), 
                                      Point(self.__x2, self.__y2)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), 
                                      Point(self.__x2, self.__y2)), "light gray",)
        if self.has_left:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), 
                                      Point(self.__x2, self.__y1)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), 
                                      Point(self.__x2, self.__y1)), "light gray",)

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        color = "gray" if undo else "red"
        self.__win.draw_line(Line(self.find_center(), to_cell.find_center()), color)
