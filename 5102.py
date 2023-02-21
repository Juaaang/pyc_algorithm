import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
def bfs(S, G):
    Q = []
    visited = [0] * (V+1)
    Q.append(S)
    visited[S] = 1
    while Q:
        v = Q.pop(0)
        for w in Gr[v]:
            if w == G:
                return visited[v]
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0
for tc in range(1,T+1):
    V, E = map(int, input().split())
    lst = []
    for _ in range(E):
        s, e = list(map(int, input().split()))
        lst.append(s)
        lst.append(e)
    S, G = map(int, input().split())
    Gr = [[] for _ in range(V + 1)]
    for idx in range(0, len(lst), 2):
        p1 = lst[idx]
        p2 = lst[idx + 1]
        Gr[p1].append(p2)
        Gr[p2].append(p1)
    print(f'#{tc}', bfs(S, G))
