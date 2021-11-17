# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:25:51 2021

@author: Tigran Boynagryan
"""


matrix = [[1,2,3],[4,5,6]]
import numpy as np

def transpose(matrix):
    mat = np.matrix(matrix).transpose()
    res = mat.tolist()
    return res

print(transpose(matrix))