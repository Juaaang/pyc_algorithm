import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        maxV = 0
        for j in range(M-N+1):
            sumT = 0
            for i in range(N):
                sumT += A[i]*B[i+j]
            if sumT > maxV :
                maxV = sumT



    else:
        maxV = 0
        for j in range(N-M+1):
            sumT = 0
            for i in range(M):
                sumT += A[i+j]*B[i]
            if sumT > maxV :
                maxV = sumT
    print(f'#{tc} {maxV}')
