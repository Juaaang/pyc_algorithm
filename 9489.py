'''
가로 세로 탐색
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
                if max_len < cnt and cnt >= 2:
                    max_len = cnt
            else:
                cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if board[j][i] == 1:
                cnt += 1
                if max_len < cnt and cnt >= 2:
                    max_len = cnt
            else:
                cnt = 0
    print(f'#{tc} {max_len}')