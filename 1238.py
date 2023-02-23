import sys
sys.stdin = open('input.txt', 'r')

T = 10

def bfs(S):
    Q = [S]
    visited[S] = 0
    while Q:
        num = Q.pop(0)
        for i in Gr[num]:
            if visited[i] == 0:
                visited[i] = visited[num] + 1
                Q.append(i)

for tc in range(1, T+1):
    length, start = map(int, input().split())
    arr = list(map(int, input().split()))
    Gr = [[] for _ in range(101)]
    visited = [0]*101
    for i in range(0, len(arr), 2):
        Gr[arr[i]].append(arr[i+1])
    bfs(start)
    a = max(visited)
    max_num = 0
    for i in range(len(Gr)):
        if visited[i] == a and max_num < i:
            max_num = i
    print(f'#{tc}', max_num)

