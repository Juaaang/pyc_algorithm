import sys
sys.stdin = open('input.txt', 'r')

def dfs(start, end):
    ST = []
    visited = [False]*(100)
    ST.append(start)
    visited[start] = True
    while ST:
        endS = ST.pop()
        visited[endS] = True
        for i in range(100):
            if not visited[i] and node[endS][i]:
                ST.append(i)
    if visited[end]:
        return 1
    else:
        return 0

for tc in range(1, 11):
    tc_num, E = map(int, input().split())
    node = [['' for _ in range(100)] for _ in range(100)]
    S = list(map(int, input().split()))
    for num in range(0, E):
        start, end = S[0+2*num], S[1+2*num]
        node[start][end] = 1
    print(f'#{tc} {dfs(0,99)}')
