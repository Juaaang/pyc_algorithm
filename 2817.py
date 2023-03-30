import sys
sys.stdin = open('input.txt', 'r')

def solve(k, curS):
    global ans
    if curS > K:
        return

    if curS == K:
        ans += 1
        return

    if k == N:
        return
    solve(k+1, curS)
    solve(k+1, curS+lst[k])

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    solve(0, 0)
    print(f'#{tc}', ans)
