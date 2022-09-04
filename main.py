# this is program to populate the matrix

import numpy as np
import pandas as pd
import math as mt
import random


class Board:
    def __init__(self, arr):
        self.x_Dim = arr.shape[0]
        self.y_Dim = arr.shape[1]
        self.tempArr = arr.copy()

    def get_x_dim(self):
        return self.x_Dim

    def get_y_dim(self):
        return self.y_Dim

    def Print_Dim(self):
        print(f"The array is: \n{self.tempArr}\n The X-Dimension is: {self.x_Dim}\n The Y-Dimension is: {self.y_Dim}")

    def rowPop(self, coord_X, coord_Y):
        for i in range(self.x_Dim):
            for j in range(self.y_Dim):
                if i == coord_X:
                    self.tempArr[coord_X][j] = 1
        return self.tempArr

    def colPop(self, coord_X, coord_Y):
        for i in range(self.x_Dim):
            for j in range(self.y_Dim):
                if j == coord_Y:
                    self.tempArr[i][coord_Y] = 1
        return self.tempArr

    def primeDiagPop(self, coord_X, coord_Y):
        aux = np.ones(max(coord_X, coord_Y))
        temp = int(mt.fabs(coord_X - coord_Y))
        np.fill_diagonal(self.tempArr[:, temp:], aux)
        return self.tempArr

    def seconDiagPop(self, coord_X, coord_Y):
        np.fill_diagonal(np.fliplr(self.tempArr[coord_X:, :coord_Y + 1]), 1)
        return self.tempArr

    def neighbourPop(self,coord_X,coord_Y):
        result = []
        for rowAdd in range(-1,2):
            newRow = coord_X + rowAdd
            if newRow >= 0 and newRow <= self.x_Dim -1:
                for colAdd in range(-1,2):
                    newCol = coord_Y + colAdd
                    if newCol >= 0 and newCol <= self.y_Dim - 1:
                        if newCol == coord_Y and newRow == coord_X:
                            continue
                        result.append((newRow,newCol))
        for i,j in result:
            self.tempArr[i][j] = 1
        return self.tempArr



if __name__ == '__main__':
    #arr = np.zeros((5, 5))
    arr = np.random.rand(5, 5)
    coord_X, coord_Y = 1, 4
    #B0 = Board(arr)

