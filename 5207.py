import sys
sys.stdin = open('input.txt', 'r')

def binarySearch(s, e):
    tmp = 0
    while s <= e:
        m = (s+e)//2
        if lst1[m] == i:
            return 1
        elif lst1[m] > i and (tmp != 'left'):
            tmp = 'left'
            e = m - 1
        elif lst1[m] < i and (tmp != 'right'):
            tmp = 'right'
            s = m + 1
        else:
            return 0
    return 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    lst1 = sorted(list(map(int, input().split())))
    ans = 0
    for i in list(map(int, input().split())):
        ans += binarySearch(0, N-1)
    print(f'#{tc}', ans)