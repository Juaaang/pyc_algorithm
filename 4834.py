T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(str, input()))
    k = 0
    for num in a:
        if int(num) > k:
            k = int(num)

    cnt_lis = [0] * (k + 1)
    for i in a:
        cnt_lis[int(i)] += 1
    preV = cnt_lis[0]
    maxV = 0
    result = 0
    for j in range(1, k+1):
        if cnt_lis[j] >= cnt_lis[j-1]:
            maxV = cnt_lis[j]
            if result <= maxV:
                numb = j
                result = maxV
    print(f"#{tc} {numb} {result}")








