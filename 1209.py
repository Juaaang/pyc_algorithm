import sys
sys.stdin = open('input.txt', 'r')

def my_max(lis):
    resV = preV = lis[0]
    for i in lis:
        if i > preV:
            maxV = i
            preV = i
            if resV < maxV:
                resV = maxV
    return resV

T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sumRow = [0]*100
    sumCol = [0]*100
    sumDiagonal = [0]*2
    resLis = []
    for i in range(100):
        sumDiagonal[0] += arr[i][i]
        sumDiagonal[1] += arr[99 - i][i]
        resLis.append(my_max(sumDiagonal))
        for j in range(100):
            sumRow[i] += arr[i][j]
    resLis.append(my_max(sumRow))
    for j in range(100):
        for i in range(100):
            sumCol[j] += arr[i][j]
    resLis.append(my_max(sumCol))
    print(f'#{tc} {my_max(resLis)}')