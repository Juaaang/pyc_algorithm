import sys
sys.stdin = open('input.txt', 'r')

def per(k, curV):
    global maxV
    if curV == 0.0:
        return

    if curV <= maxV:
        return

    if k==N:
        if maxV < curV:
            maxV = curV
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(k+1, curV*arr[i][k]*0.01)
            visited[i] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    maxV = 0.0
    per(0, 1)
    ans = maxV*100
    print(f'#{tc}', '{:.6f}'.format(ans))