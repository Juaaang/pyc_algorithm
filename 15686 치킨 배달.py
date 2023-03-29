import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i,j])
        if arr[i][j] == 2:
            chicken.append([i,j])
select_chic = list(combinations(chicken, M))
ans = 10000
i = 0
while i < len(select_chic):
    sumD = 0
    for idx in house:
        tmp = 100
        for c in range(M):
            if abs(select_chic[i][c][0]-idx[0]) + abs(select_chic[i][c][1] - idx[1]) < tmp:
                tmp = abs(select_chic[i][c][0]-idx[0]) + abs(select_chic[i][c][1] - idx[1])
        sumD += tmp
    if sumD < ans:
        ans = sumD
    i += 1

print(ans)