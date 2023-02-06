'''
부분집합 원소의 수 : N
부분집합의 합 : K
if sumN == 6:
    cnt+= 1
부분집합을 전부 찾고
sumN ==6인 경우를 찾아 카운트
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
A = []

def my_sum(lis):
    sumV = 0
    for i in lis:
        sumV += i
    return sumV

for num in range(1, 13):
    A.append(num)
for tc in range(1, T+1):
    cnt = 0
    N, K = list(map(int, input().split()))
    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == N and my_sum(subset) == K:
            cnt+= 1
    print(f'#{tc} {cnt}')