'''
가위 : 1
바위 : 2
보 : 3

재귀식 ?
'''

import sys
sys.stdin = open('input.txt', 'r')


def rsp(a, b):
    if num[b] == num[a] + 1 or (num[b] == 1 and num[a] == 3):
        return b
    else:
        return a
def func(L, R):
    if L == R:
        return L
    if L + 1 == R:
        return rsp(L,R)
    return rsp(func(L, (L+R)//2), func((L+R)//2+1, R))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int, input().split()))
    print(f'#{tc} {func(0,N-1)+1}')