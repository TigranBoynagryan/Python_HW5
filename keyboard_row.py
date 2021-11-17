# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:08:51 2021

@author: Tigran Boynagryan
"""
words = ["Hello","Alaska","Dad","Peace"]
def findWords(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    ans =[]
    for i in words:
        if set(i.lower()) <= row1:
            ans.append(i)
        elif set(i.lower()) <= row2:
            ans.append(i)
        elif set(i.lower()) <= row3:
            ans.append(i)
    
    return ans

print(findWords(words))
