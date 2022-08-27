import unittest

import numpy as np

from main import Board


# This file contains the testing for the heat maps basic operations
class TestBoard(unittest.TestCase):

    def test_board_x(self):
        arr = np.zeros((5, 5))
        B0 = Board(arr)
        self.assertEqual(B0.get_x_dim(), 5)

    def test_board_y(self):
        arr = np.zeros((5, 5))
        B0 = Board(arr)
        self.assertEqual(B0.get_y_dim(), 5)


if __name__ == '__main__':
    unittest.main()
