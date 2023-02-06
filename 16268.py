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
    for i in range(1, N-1):
        sumA = 0
        for j in range(1, M-1):
            sumA = arr[i][j] + arr[i+1][j] + arr[i-1][j] + arr[i][j+1] + arr[i][j-1]
            lis.append(sumA)
    print(f'#{tc} {my_max(lis)}')