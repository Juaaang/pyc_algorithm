'''
가로길이 = 100 ( Height 의 length )
Dump = 덤프 횟수
Height = 리스트 안의 인덱스들의 높이
해결방안
Height의 길이를 돌면서 가장 높은 값을 가장 낮은 값에 더해주고
Dump를 1 차감한다
Dump = 0 이 되었을 때의 Height 에서
리스트의 최고 높이와 최저높이의 차이를 구하는 문제
'''

def my_min(lis):
    temp = 0
    for i in lis:
        if temp == 0 or i < temp:
            temp = i
    return temp

def my_max(lis):
    temp = 0
    for i in lis:
        if temp == 0 or i > temp:
            temp = i
    return temp

T = 10
for tc in range(1, T+1):
    Dump = int(input())
    H = list(map(int, input().split()))
    while Dump > 0:
        for i in range(len(H)):       # H 의길이를 돌려서 i번째 인덱스가 max. min 이면 변경
            if H[i] == my_max(H):
                H[i] -= 1
                break
        for j in range(len(H)):
            if H[j] == my_min(H):
                H[j] += 1
                break
        Dump -= 1
        continue


    print(f'#{tc} {my_max(H) - my_min(H)}')
