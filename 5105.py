import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(si, sj):
    Q = deque([])
    visited = [[-1]*N for _ in range(N)]
    Q.append((si, sj))
    visited[si][sj] = 0
    while Q:
        ci, cj = Q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = ci+dx, cj+dy
            if 0 <= nx < N and 0<= ny < N and visited[nx][ny] == -1:
                if arr[nx][ny] == '0':
                    visited[nx][ny] = visited[ci][cj] + 1
                    Q.append((nx, ny))
                if arr[nx][ny] == '2':
                    return visited[ci][cj]
    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '3':
                start = i, j,
                break
    print(f'#{tc}', bfs(start[0], start[1]))
