import sys
sys.stdin = open('input.txt', 'r')

def merge(left, right):
    result = []
    lp = 0
    rp = 0

    while lp<len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    result.extend(left[lp:])
    result.extend(right[rp:])

    return result
def mergeS(lst):
    global cnt
    if len(lst) == 1:
        return lst

    m = len(lst)//2
    left = lst[:m]
    right = lst[m:]

    left = mergeS(left)
    right = mergeS(right)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = mergeS(lst)
    print(f'#{tc} {ans[N//2]} {cnt}')