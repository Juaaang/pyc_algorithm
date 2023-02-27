import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    s = input()
    s = int(s[2:]) / (10**(len(s)-2))
    num = 1
    ans = ''
    while s !=0 :
        if num >= 13:
            ans = 'overflow'
            break
        if s >= 2**(-num):
            s -= 2**(-num)
            ans += '1'
        else:
            ans += '0'
        num+= 1
    print(f'#{tc}', ans)


