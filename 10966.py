import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def bfs(s, e):
    Q = []
    visited = [[0]*M for _ in range(N)]
    Q.append(s)
    visited[s] =
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
