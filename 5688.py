import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    i = 1
    while True:
        if i**3 == N:
            print(f'#{tc}', i)
            break
        elif i**3 <=N:
            i += 1
        else:
            print(f'#{tc}', -1)
            break