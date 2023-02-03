'''
N = 일수
price = 각 날짜의 매매가
끝값이 낮으면 파는 것이 손해
값이 쌀때 사서 가장비싼날(최대값)에 팔고 다음최대값에 판매하는 방식

해결방안
price 를 리스트로 만들고
리스트에서 Max 값을 만나면
이전까지의 index 들을 Max 에서 빼줌
더해줌( res )
price 를 slicing 을 통해 Max 의 위치까지 잘라줌
반복
만약 price 의 길이가 1이되면 break
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def my_max(lis):
    preV = lis[0]
    resV = lis[0]
    for i in lis:
        if i > preV:
            maxV = i
            if resV < maxV:
                resV = maxV
    return resV
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    res = 0
    i = 0
    while i < len(price):
        if price[i] == my_max(price):
            for j in range(i):
                res += my_max(price) - price[j]
            price = price[i+1:]
            i = 0
            continue
        else:
            i += 1


    print(f'#{tc} {res}')







