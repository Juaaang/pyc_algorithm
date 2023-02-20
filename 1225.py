import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1,T+1):
    tc_num = int(input())
    password = list(map(int, input().split()))
    i = 0
    cnt = 0
    while password:
        t = password.pop(0) - (i+1)
        if t <= 0:
            password.append(0)
            break
        else:
            password.append(t)
        i = (i+1) % 5
    print(f'#{tc}', *password)
