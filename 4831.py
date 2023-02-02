'''
K : 한번에 최대 이동할 수 있는 정류장 수
N : 정류장의 수
M : 충전기가 설치된 정류장의 수
M_num : 충전기가 설치된 정류장의 번호

최소 충전횟수 출력

해결방안
M_num 의 차이가 3보다 크면 0을 출력
0번째 정류장에는 충전기가 설치된 상태
'''


T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_num = list(map(int, input().split()))
    cnt = 0
    i = 0
    result = 0
    while i < N:
        for j in range(i + K, i, -1):
            if j in M_num:
                cnt += 1
                break
            if j == N:
                break
        else:
            cnt = 0
            break

        i = j
        continue

    print(f'#{tc} {cnt}')




