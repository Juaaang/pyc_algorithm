'''
0000 -> 0011
000 -> 111 -> 100
만약 N이랑 base랑 다르면
    base[i] = N[i]
탈출조건
N == base

'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = list(map(str, input()))
    base = list('0'*len(N))
    cnt = 0
    for i in range(len(N)):
        if base[i] != N[i]:
            base[i:] = N[i]*(len(N)-i)
            cnt+= 1
    print(f'#{tc} {cnt}')