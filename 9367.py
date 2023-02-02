T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    result = 1
    cnt = 1
    pre_V = C[0]
    for i in range(1, N):
        if C[i] > pre_V:
            cnt += 1
            pre_V = C[i]
            if result < cnt:
                result = cnt
        else:
            cnt = 1
            pre_V =C[i]
    print(f'#{tc} {result}')

