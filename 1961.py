'''
90도, 180도, 270도 회전

회전한 board 를 만들때는 이전의 board 의 모든 값이 저장이 되어있어야 다음 상황 진행 가능
목적지 기준으로 원본의 어떤 좌표의 값이 저장되는지 확인
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    board_90 = [['0']*N for _ in range(N)]
    board_180 = [['0'] * N for _ in range(N)]
    board_270 = [['0'] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            board_90[i][j] = board[N-j-1][i]
            board_180[i][j] = board[N-1-i][N-1-j]
            board_270[i][j] = board[j][N-1-i]
    print(f'#{tc}')
    for a,b,c in zip(board_90,board_180,board_270):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)})')
    # for i in range(N):
    #     for j in range(N):
    #         board_90[i][j] = board[N-1-j][i]
    #
    # for i in range(N):
    #     for j in range(N):
    #         board_180[i][j] = board_90[N-1-j][i]
    #
    # for i in range(N):
    #     for j in range(N):
    #         board_270[i][j] = board_180[N-1-j][i]
    #
    # print(f'#{tc}')
    # for i in range(N):
    #     for a in range(N):
    #         print(board_90[i][a], end='')
    #     print(end=' ')
    #     for b in range(N):
    #         print(board_180[i][b], end='')
    #     print(end=' ')
    #     for c in range(N):
    #         print(board_270[i][c], end='')
    #     print()


