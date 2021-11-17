# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:14:33 2021

@author: Tigran Boynagryan
"""
mat = [[1,2],[3,4]]
def reshape(mat, r, c):
     
    result=[]
    result_or=[]
    or_r=len(mat)
    or_c=len(mat[0])
    if or_r*or_c!=r*c:
        return mat
    for i in range(or_r):
        for j in range(or_c):
            result_or.append(mat[i][j])
    for i in range(r):
        result_temp=[]
        for j in range(c):
            result_temp.append(result_or.pop(0))
        result.append(result_temp)
    return result

print(reshape(mat, 2, 4))