import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * 8
    for i in range(len(money)):
        if N // money[i] != 0:
            lst[i] += N // money[i]
            N -= (N // money[i]) * money[i]
    print(f'#{tc}')
    print(*lst)