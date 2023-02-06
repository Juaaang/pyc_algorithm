import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def my_max(lis):
    resV = preV = lis[0]
    for i in lis:
        if i > preV:
            maxV = i
            preV = i
            if resV < maxV:
                resV = maxV
    return resV

for tc in range(1, T+1):
    lis = []
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumA = 0
            for k in range(M):
                for l in range(M):
                    sumA += arr[i+k][j+l]
            lis.append(sumA)
    print(f'#{tc} {my_max(lis)}')