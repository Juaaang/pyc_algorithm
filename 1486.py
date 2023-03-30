import sys
sys.stdin = open('input.txt', 'r')

def solve(k, curS):
    global S
    if B <= curS < S:
        S = curS

    if k == N:
        return

    solve(k+1, curS)
    solve(k+1, curS+h_lis[k])

T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    h_lis = list(map(int, input().split()))
    h_lis.sort()
    S = 200000
    solve(0,0)
    print(f'#{tc}', S-B)
