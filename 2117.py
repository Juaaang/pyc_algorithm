'''
집과 집사이의 거리 생각
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def bfs(si, sj):
    Q = []
    visited = [[0] * N for _ in range(N)]
    Q.append((si, sj))
    visited[si][sj] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while Q:
        ci, cj = Q.pop(0)
        for d in range(4):
            newR = ci + dr[d]
            newC = cj + dc[d]
            if 0 <= newR < N and 0 <= newC < N and visited[newR][newC] == 0 and arr[newR][newC] == 1:
                visited[newR][newC] = visited[ci][cj] + 1
                Q.append((newR, newC))

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                bfs(i, j)
