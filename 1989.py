import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def isPelindrome(s):
    s = s.rstrip()
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS//2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1
for tc in range(1,T+1):
    txt = input()
    print(f'#{tc} {isPelindrome(txt)}')

