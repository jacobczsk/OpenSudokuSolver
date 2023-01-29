import unittest
import src.OpenSudokuSolver as oss


class TestOSS(unittest.TestCase):
    def test_solve_simple(self):
        board = [
            [None, 8, 7, None, 1, 5, 9, None, None],
            [None, None, 2, 7, 6, 3, 1, None, None],
            [5, None, None, 9, None, None, None, 4, None],
            [9, 4, None, None, None, None, 5, None, 3],
            [None, 7, 5, None, None, None, 6, 9, None],
            [None, 3, None, 5, None, 9, 8, 7, 2],
            [None, None, None, 1, None, None, None, 6, 9],
            [None, None, None, 3, None, 6, 2, None, None],
            [None, 6, None, None, 8, 4, 7, 3, None],
        ]
        solved = [
            [3, 8, 7, 4, 1, 5, 9, 2, 6],
            [4, 9, 2, 7, 6, 3, 1, 5, 8],
            [5, 1, 6, 9, 2, 8, 3, 4, 7],
            [9, 4, 8, 6, 7, 2, 5, 1, 3],
            [2, 7, 5, 8, 3, 1, 6, 9, 4],
            [6, 3, 1, 5, 4, 9, 8, 7, 2],
            [8, 2, 3, 1, 5, 7, 4, 6, 9],
            [7, 5, 4, 3, 9, 6, 2, 8, 1],
            [1, 6, 9, 2, 8, 4, 7, 3, 5],
        ]
        self.assertEqual(oss.solve(board)[0], solved)

    def test_solve_medium(self):
        board = [
            [None, None, None, 8, None, None, 4, None, None],
            [None, None, None, None, None, None, 3, 1, None],
            [None, None, None, None, None, None, None, 5, 2],
            [2, 8, None, None, None, None, 9, None, None],
            [1, None, None, 4, None, None, None, None, None],
            [None, None, 5, 6, None, None, 8, None, None],
            [8, None, None, 5, 6, None, None, 3, None],
            [None, 3, None, None, None, None, None, 2, None],
            [5, None, 4, None, 1, 3, None, None, 6],
        ]
        solved = [
            [3, 6, 2, 8, 5, 1, 4, 9, 7],
            [4, 5, 9, 7, 2, 6, 3, 1, 8],
            [7, 1, 8, 3, 4, 9, 6, 5, 2],
            [2, 8, 6, 1, 7, 5, 9, 4, 3],
            [1, 7, 3, 4, 9, 8, 2, 6, 5],
            [9, 4, 5, 6, 3, 2, 8, 7, 1],
            [8, 2, 7, 5, 6, 4, 1, 3, 9],
            [6, 3, 1, 9, 8, 7, 5, 2, 4],
            [5, 9, 4, 2, 1, 3, 7, 8, 6],
        ]
        self.assertEqual(oss.solve(board)[0], solved)

    def test_solve_hard(self):
        board = [
            [None, 5, None, None, 6, None, None, None, None],
            [None, None, None, 8, None, None, None, None, None],
            [None, None, None, 2, None, None, 4, None, 8],
            [None, 2, None, None, 5, None, None, None, 1],
            [None, None, None, None, None, 6, 9, None, None],
            [9, None, 1, 3, None, None, None, 5, None],
            [3, None, None, None, 4, None, None, None, None],
            [None, None, None, 5, None, 3, None, 1, None],
            [5, None, None, None, 8, 9, 6, 4, None],
        ]
        solved = [
            [7, 5, 8, 4, 6, 1, 3, 9, 2],
            [2, 9, 4, 8, 3, 7, 1, 6, 5],
            [1, 6, 3, 2, 9, 5, 4, 7, 8],
            [6, 2, 7, 9, 5, 4, 8, 3, 1],
            [8, 3, 5, 7, 1, 6, 9, 2, 4],
            [9, 4, 1, 3, 2, 8, 7, 5, 6],
            [3, 1, 9, 6, 4, 2, 5, 8, 7],
            [4, 8, 6, 5, 7, 3, 2, 1, 9],
            [5, 7, 2, 1, 8, 9, 6, 4, 3],
        ]
        self.assertEqual(oss.solve(board)[0], solved)

    def test_solve_Escargot(self):
        board = [
            [1, None, None, None, None, 7, None, 9, None],
            [None, 3, None, None, 2, None, None, None, 8],
            [None, None, 9, 6, None, None, 5, None, None],
            [None, None, 5, 3, None, None, 9, None, None],
            [None, 1, None, None, 8, None, None, None, 2],
            [6, None, None, None, None, 4, None, None, None],
            [3, None, None, None, None, None, None, 1, None],
            [None, 4, None, None, None, None, None, None, 7],
            [None, None, 7, None, None, None, 3, None, None],
        ]
        solved = [
            [1, 6, 2, 8, 5, 7, 4, 9, 3],
            [5, 3, 4, 1, 2, 9, 6, 7, 8],
            [7, 8, 9, 6, 4, 3, 5, 2, 1],
            [4, 7, 5, 3, 1, 2, 9, 8, 6],
            [9, 1, 3, 5, 8, 6, 7, 4, 2],
            [6, 2, 8, 7, 9, 4, 1, 3, 5],
            [3, 5, 6, 4, 7, 8, 2, 1, 9],
            [2, 4, 1, 9, 3, 5, 8, 6, 7],
            [8, 9, 7, 2, 6, 1, 3, 5, 4],
        ]
        self.assertEqual(oss.solve(board)[0], solved)
