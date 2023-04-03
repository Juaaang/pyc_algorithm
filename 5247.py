import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(curV):
    cnt = 0
    q = deque([])
    q.append((curV, cnt))
    visited = [False]*1000001
    while q:
        tmp, cnt = q.popleft()
        for i in (tmp+1, tmp-1, tmp*2, tmp-10):
            if i == M:
                cnt += 1
                return cnt

            if 0 <= i < 1000000 and not visited[i]:
                visited[i] = True
                q.append((i, cnt+1))

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{tc}', bfs(N))