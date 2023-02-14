'''
방향성이 있는 문제
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(start, end):
    ST = []
    visited = [False]*(V+1)
    ST.append(start)
    visited[start] = True
    while ST:
        endS = ST.pop()
        visited[endS] = True
        for i in range(1, V+1):
            if not visited[i] and node[endS][i]:
                ST.append(i)
    if visited[end]:
        return 1
    else:
        return 0



for tc in range(1,T+1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S,G)}')
