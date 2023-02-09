'''
첫글씨가 같고 두번째 글씨가 다른 조건
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    i = 0
    cnt = 0

    while i < N:
        if A[i] == B[0]:
            if A[i:i+M] == B:
                cnt += 1
                i += M
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1
    print(f'#{tc} {cnt}')