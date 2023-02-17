'''
입력의 좌표를 보고 패딩을 해야 편하다는 것을 눈치채야 함
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    c = N // 2
    arr[c][c] = arr[c+1][c+1] = 2
    arr[c][c+1] = arr[c+1][c] = 1
    dr = [0, 1, 1, 1, 0, -1, -1, -1]         #오른쪽부터
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    d = 0
    for _ in range(M):
        si, sj, stone = map(int, input().split())
        arr[si][sj] = stone
        for d in range(8):
            ST = []
            for i in range(1, N):
                newR = si + dr[d]*i
                newC = sj + dc[d]*i
                if arr[newR][newC] == 0:
                    break
                elif arr[newR][newC] != stone:
                    ST.append((newR,newC))
                else:
                    while ST:
                        st_i, st_j = ST.pop()
                        arr[st_i][st_j] = stone
                    break

    b_stone = 0
    w_stone = 0
    for lst in arr:
        b_stone += lst.count(1)
        w_stone += lst.count(2)

    print(f'#{tc} {b_stone} {w_stone}')













    # arr =[[0]*(N+2) for _ in range(N+2)]
    # m = N // 2
    # arr[m][m] = arr[m+1][m+1] = 2
    # arr[m+1][m] = arr[m][m+1] = 1
    #
    # for _ in range(M):
    #     si, sj, d = map(int, input().split())
    #     arr[si][sj] = d
    #     for di, dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
    #         tlst = []
    #         for mul in range(1,N):
    #             ni, nj = si + di*mul, sj+dj*mul
    #             if arr[ni][nj] == 0:
    #                 break
    #             elif arr[ni][nj] != d:
    #                 tlst.append((ni,nj))
    #             else:
    #                 while tlst:
    #                     ti, tj = tlst.pop()
    #                     arr[ti][tj]=d
    #                 break
    # bcnt = wcnt = 0
    # for lst in arr:
    #     bcnt += lst.count(1)
    #     wcnt += lst.count(2)
    #
    #
    #
    # print(f'#{tc} {bcnt} {wcnt}')