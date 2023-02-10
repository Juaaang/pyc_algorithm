import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
def check(lis, N, M, K):
    for i in range(N):
        if (lis[i]//M)*K -(i+1) < 0:
            return 0
    return 1
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    N_t = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if N_t[j] > N_t[j+1]:
                N_t[j], N_t[j+1] = N_t[j+1], N_t[j]
    if check(N_t, N, M, K) == 1:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')

