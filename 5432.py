'''
쇠막대기 자르기
레이저를 쏠 때 스택에 '(' 가 쌓여있는 만큼 cnt
')'로 닫힐때 1씩 cnt
'''

import sys
sys.stdin = open('input.txt', 'r')

T= int(input())

for tc in range(1,T+1):
    s = input()
    ST = []
    piece = 0
    for i in range(len(s)):
        if s[i] == '(':
            ST.append(i)

        else:
            if s[i-1] == '(':
                ST.pop()
                piece += len(ST)
            else:
                ST.pop()
                piece += 1
    print(f'#{tc} {piece}')













    # res = 0
    # cnt = 0
    # for i in range(len(s)):
    #     if s[i] == '(':
    #         cnt += 1
    #     else:
    #         if s[i-1] == '(':
    #             cnt -= 1
    #             res += cnt
    #         else:
    #             cnt -= 1
    #             res += 1
    # print(f'#{tc} {res}')