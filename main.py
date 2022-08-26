# this is program to populate the matrix

import numpy as np
import pandas as pd
import math as mt
import random


def rowPop(arr, coord_X, coord_Y):
    tempArr = arr.copy()
    x_Dim = tempArr.shape[0]
    y_Dim = tempArr.shape[1]
    for i in range(x_Dim):
        for j in range(y_Dim):
            if i == coord_X:
                tempArr[coord_X][j] = 1
    return tempArr


def colPop(arr, coord_X, coord_Y):
    tempArr = arr.copy()
    x_Dim = tempArr.shape[0]
    y_Dim = tempArr.shape[1]
    for i in range(x_Dim):
        for j in range(y_Dim):
            if j == coord_Y:
                tempArr[i][coord_Y] = 1
    return tempArr


def primeDiag(arr, coord_X, coord_Y):
    tempArr = arr.copy()
    aux = np.ones(max(coord_X, coord_Y))
    temp = int(mt.fabs(coord_X - coord_Y))
    np.fill_diagonal(tempArr[:, temp:], aux)
    return tempArr


def seconDiag(arr, coord_X, coord_Y):
    tempArr = arr.copy()
    x_Dim = tempArr.shape[0]
    y_Dim = tempArr.shape[1]
    

# arr = np.zeros((5,5))
arr = np.random.rand(5, 5)
coord_X, coord_Y = 1, 4
# arr = rowPop(arr,coord_X,coord_Y)
# arr = colPop(arr,coord_X,coord_Y)
# arr = primeDiag(arr,coord_X,coord_Y)
# print(arr)
seconDiag(arr, coord_X, coord_Y)
