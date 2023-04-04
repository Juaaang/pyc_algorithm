import sys
sys.stdin = open('input.txt', 'r')


def find_set(x):
    while x != A[x]:
        x = A[x]
    return x

def union(x, y):
    A[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    A = [i for i in range(V+1)]
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append([w,n1,n2])
    graph.sort()

    ans = cnt = 0
    for w, n1, n2 in graph:
        if find_set(n1) != find_set(n2):
            cnt += 1
            ans += w
            union(n1, n2)
            if cnt == V:
                break
    print(f'#{tc}', ans)
