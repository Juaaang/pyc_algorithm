'''
벡터연산
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    d = 0
    res = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for d in range(8):
                newR = i + dr[d]
                newC = j + dc[d]
                if 0<= newR < N and 0<= newC < M and arr[newR][newC] < arr[i][j]:
                    cnt += 1
            if cnt >= 4:
                res += 1
    print(f'#{tc} {res}')



