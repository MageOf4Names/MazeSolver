import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows,
        )    

    def test_maze_break_entrace_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[m1.rows - 1][m1.cols - 1].has_bottom,
            False,
        )

    def test_maze_visit_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()
