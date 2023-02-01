T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    lis = [0]*(N-M+1)
    for i in range(N-M+1):
        sumV = 0
        for j in range(i, i+M):
            sumV += a[j]
            lis[i] = sumV

    minV = lis[0]
    maxV = lis[0]
    for k in lis:
        if k > maxV:
            maxV = k
        if k < minV:
            minV = k

    print(f'#{tc} {maxV - minV}')
