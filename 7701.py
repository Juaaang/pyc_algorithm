'''
염라대왕의 이름 정렬
길이가 긴 문자열은 아래로, 짧은 문자열은 위로
문자열의 첫번째 자리부터 비교하며 사전순 정렬( sort()활용)
문자열의 길이가 같을 때,
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(set([input() for _ in range(N)]))
    arr.sort(key=lambda x: (len(x),x))
    print(f'#{tc}')
    for i in arr:
        print(i)
