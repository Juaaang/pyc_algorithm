import sys
sys.stdin = open('input.txt', 'r')

def go_dijkstra(X):
    D = [0] * (N + 1)
    U = [0]*(N+1)
    U[X] = 1
    for i in range(N+1):
        D[i] = adjM[X][i]

    for _ in range(N-1):
        minV = INF
        w = 0
        for j in range(N+1):
            if U[j] == 0 and minV > D[j]:
                w = j
                minV = D[j]
        U[w] = 1
        for v in range(N+1):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w]+adjM[w][v])
    return D

def back_dijkstra(X):
    D = [0] * (N + 1)
    U = [0] * (N + 1)
    U[X] = 1
    for i in range(N + 1):
        D[i] = adjM[i][X]

    for _ in range(N - 1):
        minV = INF
        w = 0
        for j in range(N + 1):
            if U[j] == 0 and minV > D[j]:
                w = j
                minV = D[j]
        U[w] = 1
        for v in range(N + 1):
            if 0 < adjM[v][w] < INF:
                D[v] = min(D[v], D[w] + adjM[v][w])
    return D

INF = 100000
for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adjM[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        adjM[x][y] = c
    ans1 = go_dijkstra(X)
    ans2 = back_dijkstra(X)
    ans = 0
    for i in range(1, N+1):
        ans = max(ans, ans1[i]+ans2[i])
    print(f'#{tc}', ans)
