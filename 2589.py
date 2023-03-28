'''
L인 지점을 출발점으로 인접좌표 탐색하며
방문표시해주면서 이동하다가 최대 이동거리 구함
전체 탐색해주면서 최대 이동거리 출력
'''


import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(x,y):
    d = 0
    q = deque([])
    q.append([x,y])
    visited[x][y] = d
    while q:
        x, y = q.popleft()
        d = visited[x][y]
        for direc in range(4):
            newR = x + dr[direc]
            newC = y + dc[direc]
            if 0 <= newR < Y and 0 <= newC < X and arr[newR][newC] == 'L' and visited[newR][newC] == -1:
                q.append([newR,newC])
                visited[newR][newC] = d+1
    return d

Y, X = map(int, input().split())
arr = [list(map(str, input())) for _ in range(Y)]
ans = 0
for i in range(Y):
    for j in range(X):
        visited = [[-1]*X for _ in range(Y)]
        if arr[i][j] == 'L':
            ans = max(ans, bfs(i,j))

print(ans)

# def bfs(x, y):
#     t = 0
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = t
#
#     while queue:
#         x, y = queue.popleft()
#         t = visited[x][y]
#
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#
#             if not (-1 < nx < n and -1 < ny < m):
#                 continue
#
#             if visited[nx][ny] != -1:
#                 continue
#
#             if area[nx][ny] == "W":
#                 continue
#
#             queue.append((nx, ny))
#             visited[nx][ny] = t + 1
#
#     return t
#
#
# n, m = map(int, input().split())
#
# area = []
#
# for _ in range(n):
#     area.append(list(input()))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# result = 0
#
# for i in range(n):
#     for j in range(m):
#         if area[i][j] == "L":
#             visited = [[-1] * m for _ in range(n)]
#             result = max(result, bfs(i, j))
#
# print(result)