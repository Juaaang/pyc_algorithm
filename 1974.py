'''
가로세로 / 격자 2가지 상황을 나눠서 문제 해결


'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        for j in range(9):
            rowIdx = board[i][j]
            colIdx = board[j][i]
            if row_check[rowIdx] == 0:
                row_check[rowIdx] = 1
            else:
                result = 0
            if col_check[colIdx] == 0:
                col_check[colIdx] = 1
            else:
                result = 0
            if i % 3 == 0 and j % 3 == 0:
                box_check = [0] * 10
                for k in range(3):
                    for l in range(3):
                        boxIdx = board[k+i][l+j]
                        if box_check[boxIdx] == 0:
                            box_check[boxIdx] = 1
                        else:
                            result = 0
    print(f'#{tc} {result}')
