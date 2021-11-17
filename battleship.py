# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:22:52 2021

@author: Tigran Boynagryan
"""
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
def countBattleships(board) -> int:
    if not board:
        return 0
    
    count = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                continue
            if i > 0 and board[i - 1][j] == "X":
                continue
            if j > 0 and board[i][j - 1] == "X":
                continue
            count += 1

           
    return count

print(countBattleships(board))