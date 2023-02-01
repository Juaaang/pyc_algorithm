# SW Expert 1206번
'''
test case
0 0 3 5 2 4 9 0 6 4 0 6 0 0    #6이 정답
조망권 확보된 세대의 공통점 : 리스트 안의 길이 2차이 중 가장 큰값과의 차이
idx가 idx -2 와 idx + 2 중 큰값과 비교해서 빼기
for i in range(2, N-2):
    for j in range(2, H-2):
    if j
'''


for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))
    sumV = 0
    for i in range(2, N-2):   # N 개의 건물을 돌면서
        a = 0
        aMax = 0
        cnt = 0
        for j in range(i-2, i+3):   # i 번째부터 i+4 까지의 높이들중 가운데 값인 i+2 보다 모두가 작으면 더한다
            if H[i] > H[j]:     # 만약 중간 값이 j (0~4) 보다 크다면 카운트( 본인은 무조건 아니기때문에 4가 최대)
                cnt += 1
                a = H[j]
                if aMax < a:
                    aMax = a
        if cnt == 4:
            sumV += (H[i] - aMax)
    print(f'#{tc} {sumV}')

