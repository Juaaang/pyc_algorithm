'''
벡터연산
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row = 0
    col = 0
    cnt = 0
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    d = 0
    while row < N:
        newR = row + dr[d]
        newC = col + dc[d]
        if 0 <= newR < N and 0 <= newC < N and arr[row][col] > arr[newR][newC]:
            d = (d + 1) % 8
            cnt += 1
            continue
        d = (d + 1) % 8

