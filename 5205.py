import sys
sys.stdin = open('input.txt', 'r')


def hoare(l, r):
    p = l
    lp = l + 1
    rp = r
    while lp <= rp:
        while lp <= rp and lst[lp] <= lst[p]:
            lp += 1
        while lp <= rp and lst[rp] >= lst[p]:
            rp -= 1
        if lp < rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[p], lst[rp] = lst[rp], lst[p]

    return rp

def quickS(l, r):
    if l < r:
        p = hoare(l,r)
        quickS(l, p - 1)
        quickS(p + 1, r)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quickS(0, len(lst) - 1)
    print(f'#{tc} {lst[N//2]}')
