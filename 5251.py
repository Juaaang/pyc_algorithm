import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(s, N):
    U = [0]*(N+1)
    U[s] = 1
    for a in range(N+1):
        D[a] = adjM[s][a]

    for b in range(N):
        minV = 10
        w = 0
        for c in range(N+1):
            if U[c] == 0 and minV > D[c]:
                w = c
                minV = D[c]
        U[w] = 1
        for v in range(N+1):
            if 0 < adjM[w][v] < 10:
                D[v] = min(D[v], D[w]+adjM[w][v])


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    adjM = [[10]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    D = [0]*(N+1)
    dijkstra(0,N)
    print(f'#{tc}', D[N])