import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    cnt = 0
    for i in range(M-N+1):
        if str1 == str2[i:N+i]:
            cnt += 1
    print(f'#{tc} {cnt}')
