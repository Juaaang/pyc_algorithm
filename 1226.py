import sys
sys.stdin = open('input.txt', 'r')

T = 10

def bfs(i,j):
    Q = []
    visited = [[-1]*16 for _ in range(16)]
    Q.append((i,j))
    visited[i][j] = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while Q:
        ci, cj = Q.pop(0)
        for d in range(4):
            newR = ci + dr[d]
            newC = cj + dc[d]
            if 0<= newR < 16 and 0 <= newC < 16 and arr[newR][newC] == '0' and visited[newR][newC] == -1:
                visited[newR][newC] = visited[ci][cj] + 1
                Q.append((newR, newC))
            if 0 <= newR < 16 and 0 <= newC < 16 and visited[newR][newC] == -1 and arr[newR][newC] == '3':
                return 1
    return 0


for tc in range(1,T+1):
    tc_num = int(input())
    arr = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                start = i, j,
                break
    print(f'#{tc}', bfs(start[0], start[1]))