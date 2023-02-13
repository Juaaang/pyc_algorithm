import sys
sys.stdin = open('input.txt', 'r')

def recur(M, N):
    if M == 1:
        return N
    if M == 0:
        return 1
    return N * recur(M-1, N)


T = 10
for tc in range(1,T+1):
    tc_num = int(input())
    N, M = map(int, input().split())
    print(f'#{tc_num} {recur(M, N)}')
