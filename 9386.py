# 9386 문제풀이

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))
    cnt = 0
    maxV = 0
    result = 0
    for i in a:
        if i == 1:
            cnt += 1
            maxV = cnt
        else:
            cnt = 0
        if result < maxV:
            result = maxV


    print(f'#{tc} {result}')
