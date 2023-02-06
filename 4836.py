'''
색깔 : box[-1] 인덱스
색깔이 다를 때, 저장값이 다른 색에 있으면 카운트

'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    lst_r = []
    lst_b = []
    cnt = 0
    for num in range(N):
            for i in range(box[num][2] - box[num][0]+1):
                for j in range(box[num][3] - box[num][1]+1):
                    new_i = i + box[num][0]
                    new_j = j + box[num][1]
                    if box[num][-1] == 1:
                        lst_r.append([new_i, new_j])
                    if box[num][-1] == 2:
                        lst_b.append([new_i, new_j])
    for k in lst_r:
        if k in lst_b:
            cnt += 1
    print(f'#{tc} {cnt}')
