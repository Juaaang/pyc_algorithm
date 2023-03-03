'''
비어있으면 내리기(row++)

'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    board = [list(input().split()) for _ in range(5)]
    new_str = ''
    for j in range(5):
        for i in range(5):
            new_str += board[i][j]
