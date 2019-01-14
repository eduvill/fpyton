# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""

#%%
# Sequence에 덧셈,곱셈 연산자 사용
l1 = [1, 2, 3]
#l2 = l1 + 3  # error
l2 = l1 + [4, 5]
print(l2)
l3 = l1 * 3
print(l3)

l4 = 3 * 'abcde'
print(l4)

#%%
# 리스트의 리스트 만들기
# nested list를 초기화하는 경우
# - 학생들을 팀별로 리스트로 묶는 경우
# - 게임판의 정사각형을 표현하는 경우
board = [['_'] * 3 for i in range(4)]
print(len(board))
print(board)

board[1][2] = 'X'
print(board)

print(id(board[0]), id(board[1]), id(board[2]), id(board[3]))

#%%
# 동일한 리스트에 대한 3개의 참조를 갖는 리스트
weird_board = [['_']*3] * 4
print(len(weird_board))
print((weird_board))

weird_board[1][2] = 'X'
#weird_board[2][2] = 'O'
print((weird_board))

print(id(weird_board[0]), id(weird_board[1]), id(weird_board[2]), id(weird_board[3]))

#%%
# 동일한 리스트에 대한 3개의 참조를 갖는 리스트
row = ['_'] * 3
board = []
for i in range(4):
    board.append(row)
print(board)
board[1][2] = 'X'
#board[2][2] = 'O'
print(board)

print(id(board[0]), id(board[1]), id(board[2]), id(board[3]))
#%%