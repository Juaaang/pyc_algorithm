import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        r, c = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N:
                gap = 0
                if arr[nx][ny] - arr[r][c] > 0:
                    gap = arr[nx][ny] - arr[r][c]

                if visited[nx][ny] > visited[r][c] + 1 + gap:
                    visited[nx][ny] = visited[r][c] + gap + 1
                    q.append((nx, ny))

    return visited[N-1][N-1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[10000000] * N for _ in range(N)]
    print(f'#{tc}', bfs(0, 0))