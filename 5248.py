import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lis = list(map(int, input().split()))
    rep = [i for i in range(N+1)]
    for i in range(M):
        union(lis[2*i], lis[2*i+1])
    ans = set()
    for i in range(1, N+1):
        ans.add(find_set(rep[i]))
    print(f'#{tc}', len(ans))




