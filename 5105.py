import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def bfs(si, sj, arr):
    Q = []
    visited = [[-1]*N for _ in range(N)]
    Q.append((si, sj))
    visited[si][sj] = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while Q:
        ci, cj = Q.pop(0)
        for d in range(4):
            newR = ci + dr[d]
            newC = cj + dc[d]
            if 0 <= newR < N and 0<= newC < N and arr[newR][newC] == '0' and visited[newR][newC] == -1:
                visited[newR][newC] = visited[ci][cj] + 1
                Q.append((newR, newC))
            if 0 <= newR < N and 0<= newC < N and visited[newR][newC] == -1 and arr[newR][newC] == '2':
                return visited[ci][cj]
    return 0


for tc in range(1,T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '3':
                start = i, j,
                break
    print(f'#{tc}', bfs(start[0], start[1], arr))
