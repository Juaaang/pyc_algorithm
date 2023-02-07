'''
0 2 4 6 8 index에 최대값 순
1 3 5 7 9 index에 최소값 순
arr 크기 만큼 돌면서
크면 0 2 4 순
작으면 1 3 5 순
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        maxIdx = i
        minIdx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if arr[maxIdx] < arr[j]:
                    maxIdx = j
            arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
        else:
            for k in range(i+1, N):
                if arr[minIdx] > arr[k]:
                    minIdx = k
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
    if len(arr) > 10:
        arr = arr[:10]
    print(f'#{tc}', *arr)
