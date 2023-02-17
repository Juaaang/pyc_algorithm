'''
N = 일수
price = 각 날짜의 매매가
끝값이 낮으면 파는 것이 손해
값이 쌀때 사서 가장비싼날(최대값)에 팔고 다음최대값에 판매하는 방식

해결방안
뒤에서부터 최대값이면 그 다음 최대값이 나오기 전까지 차이를 누적해서 출력
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    res = 0
    curMax = 0
    for i in price[::-1]:
        if curMax > i:
            res += curMax - i
        else:
            curMax = i
    print(f'#{tc} {res}')

    # 해결법2.
    # i = 0
    # res = 0
    # while i < N:
    #     i_max = i
    #     for j in range(i+1, N):
    #         if price[i_max] < price[j]:
    #             i_max = j
    #
    #     for j in range(i, i_max):
    #         res += price[i_max] - price[j]
    #
    #     i = i_max + 1
    print(f'#{tc} {res}')







