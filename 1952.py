import sys
sys.stdin = open('input.txt', 'r')

def backtrack(idx, curS, op):
    global minV
    if curS > year:
        return

    if idx > len(lst) or (idx == 12 and op == False):
        return

    if idx == 11:
        curS += res[idx]
        if curS < minV:
            minV = curS

    if idx == 12 and op:
        if curS < minV:
            minV = curS
    backtrack(idx+1, curS+res[idx], False)
    backtrack(idx+3, curS+month_3, True)

    return minV

T = int(input())
for tc in range(1,T+1):
    day, month, month_3, year = map(int, input().split())
    lst = list(map(int, input().split()))
    res = []
    ans = []
    minS = year
    for i in lst:
        if i:
            res.append(min(i*day, month))
        else:
            res.append(0)
    res.extend([0,0])
    minV = 10000
    ans = backtrack(0, 0, False)

    if ans < year:
        print(f'#{tc}', ans)
    else:
        print(f'#{tc}', year)