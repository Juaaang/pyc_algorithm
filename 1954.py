import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    row = col = 0
    d = 0
    for i in range(1, N**2+1):
        arr[row][col] = i
        newR = row + dr[d]
        newC = col + dc[d]
        if newR < 0 or newC < 0 or newR >= N or newC >= N or arr[newR][newC] != 0:
            d = (d+1) % 4
        row += dr[d]
        col += dc[d]
    print(f'#{tc}')
    for j in range(N):
        print(*arr[j])

# 좌표 체크 먼저하고, 밸류 체크 뒤에
