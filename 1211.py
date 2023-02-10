'''
출발해서 내려가면서
좌 or 우 가 1이면 옆으로 그리고 옆으로 간 만큼 카운트
범위 내 체크 (좌우를 0으로 감쌈)
ans - 1
좌/우 1순위, 진행방향(dj)으로 직진

'''

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())
    board = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100*100
    for sj in range(1, 101):
        si = 0
        if board[si][sj] != 1:
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci < 99:
            cnt += 1
            if dj == 0:
                if board[ci][cj-1] == 1:
                    dj = -1
                    cj -= 1
                elif board[ci][cj+1] == 1:
                    dj = 1
                    cj += 1
                else:
                    ci += 1
            else:
                if board[ci][cj + dj] == 1:
                    cj += dj
                else:
                    dj = 0
                    ci += 1
        if mn >= cnt:
            mn, ans = cnt, sj-1
    print(f'#{tc} {ans}')