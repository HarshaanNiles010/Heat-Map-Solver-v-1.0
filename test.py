import unittest

import numpy as np

from main import Board,Player


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

    def test_check_Row_Win(self):
        arr = np.zeros((5,5))
        P0 = Player(arr)
        pass

    def test_check_Col_Win(self):
        pass

    def test_check_Pdi_Win(self):
        pass

    def test_check_Sdi_Win(self):
        pass


if __name__ == '__main__':
    unittest.main()
