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
        arr = [
           ['B','B','B','B','B'],
           ['0.0','0.0','0.0','0.0','0.0'],
           ['0.0', '0.0', '0.0', '0.0', '0.0'],
           ['0.0', '0.0', '0.0', '0.0', '0.0'],
           ['0.0', '0.0', '0.0', '0.0', '0.0'],
               ]
        arr = np.array(arr)
        P0 = Player(arr)
        self.assertEqual(P0.checkRowWin(),'B')

    def test_check_Col_Win(self):
        arr = [
            ['W', 'B', 'B', 'B', 'B'],
            ['W', '0.0', '0.0', '0.0', '0.0'],
            ['W', '0.0', '0.0', '0.0', '0.0'],
            ['W', '0.0', '0.0', '0.0', '0.0'],
            ['W', '0.0', '0.0', '0.0', '0.0'],
        ]
        arr = np.array(arr)
        P0 = Player(arr)
        self.assertEqual(P0.checkColWin(), 'W')

    def test_check_Pdi_Win(self):
        pass

    def test_check_Sdi_Win(self):
        pass


if __name__ == '__main__':
    unittest.main()
