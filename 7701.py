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
    arr = [list(input()) for _ in range(N)]
    res = []
    print(f'#{tc}')
    for idx in range(N):
        if res !=[] and arr[idx] == res[-1]:
            res.pop()
        else:
            res.append(arr[idx])
    res.sort()
    for i in range(len(res)):
        print(f'{"".join(res[i])}')