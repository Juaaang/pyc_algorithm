'''
str1 을 딕셔너리로 바꿔주고
str2 값이 딕셔너리에 있을때마다 밸류값에 카운트
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    dic = {}
    str1 = input()
    str2 = input()
    for idx in str1:
        dic[idx] = 0
    for i in str2:
        if i in dic.keys():
            dic[i] += 1

    print(f'#{tc} {max(dic.values())}')
