import sys
sys.stdin = open('input.txt', 'r')

def solve(k, curS, kcal):
    global maxV
    if k > N:
        return

    if kcal > L:
        return
    if k == N:
        if curS > maxV:
            maxV = curS
        return
    solve(k+1, curS, kcal)
    solve(k+1, curS+lis[k][0], kcal+lis[k][1])

    return maxV
T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split())
    lis = []
    for i in range(N):
        TK = list(map(int, input().split()))
        lis.append(TK)
    maxV = 0
    solve(0, 0, 0)
    print(f'#{tc}', maxV)