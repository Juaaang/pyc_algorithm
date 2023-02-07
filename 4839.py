import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = []
    P, Pa, Pb = list(map(int, input().split()))
    for num in range(1, P+1):
        arr.append(num)
    lis = [Pa, Pb]
    res = []
    for j in lis:
        cnt = 0
        left = 1
        right = P
        while left <= right:
            if P == 1 or P == 2:
                break
            c = int((left + right) / 2)
            cnt += 1
            if arr[c-1] == j:
                break
            elif arr[c-1] > j:
                right = c
            else:
                left = c
        res.append(cnt)
    if res[0] > res[1]:
        print(f'#{tc} B')
    elif res[0] < res[1]:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')






