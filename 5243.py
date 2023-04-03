import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lis = list((map(int, input().split())))
    visited = [False]*(N+1)
    arr = [[] for _ in range(N+1)]
    for i in range(0, M*2, 2):
        arr[lis[i]].append(lis[i+1])
        arr[lis[i+1]].append(lis[i])
    cnt = 0

    print(f'#{tc}', cnt)
