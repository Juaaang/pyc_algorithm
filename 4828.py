T= int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    minV = a[0]
    maxV = a[0]
    for i in range(N):
        if maxV < a[i]:
            maxV = a[i]
        if minV > a[i]:
            minV = a[i]

    print(f'#{tc} {maxV - minV}')