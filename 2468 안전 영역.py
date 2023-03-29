'''
arr의 최대값(높이) 우선 찾고,
장마비의 양을 반복하면서
해당값 찾고 max 출력
'''


import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(x,y, rain_h):
    q = deque([])
    q.append([x,y])
    if arr[x][y] > rain_h:
        visited[x][y] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            newR = r + dr[d]
            newC = c + dc[d]
            if 0<= newR < N and 0<= newC < N and arr[newR][newC]>rain_h and not visited[newR][newC]:
                q.append([newR,newC])
                visited[newR][newC] = True

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
maxH = 0
for i in range(N):
    maxH = max(maxH, max(arr[i]))

ans = 1
for h in range(1, maxH+1):
    visited = [[False] * N for _ in range(N)]
    t_ans = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b] > h and not visited[a][b]:
                bfs(a,b,h)
                t_ans += 1
    if t_ans > ans:
        ans = t_ans

print(ans)
