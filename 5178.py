import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
    for _ in range(M):
        node, num = map(int, input().split())
        arr[node] = num
    last = N
    while last > 1:
        p = last // 2
        if (last-1) // 2 == p:
            arr[p] = arr[last] + arr[last - 1]
            last -= 2
        else:
            arr[p] = arr[last]
            last -= 1
    print(f'#{tc}', arr[L])