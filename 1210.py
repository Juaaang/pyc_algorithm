# Ladder1

import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dr = [0, 0, -1]
    dc = [-1, 1, 0]    #좌 , 우 , 위
    row = 99
    col = 0
    for i in range(100):
        if arr[row][i] == 2:
            col = i
    d = 0
    while row > 0:
        newR = row + dr[d]
        newC = col + dc[d]
        if newR < 0 or newC < 0 or newR >= 100 or newC >= 100 or arr[newR][newC] != 1:
            d = (d+1) % 3
            continue
        else:
            arr[row][col] -= 1
            row = row + dr[d]
            col = col + dc[d]
            d = 0
    print(f'#{tc} {col}')
