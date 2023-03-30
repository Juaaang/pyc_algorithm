import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stat = [list(map(int, input().split())) for _ in range(N)]
    newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
    allstat = sum(newstat) // 2
    result = float('inf')
    for l in combinations(newstat, N//2):
        result = min(result, abs(allstat - sum(l)))
    print(f'#{tc}', result)


# def my_sum(i,j, arr, lis):
#     return arr[lis[i]][lis[j]] + arr[lis[j]][lis[i]]
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     nums = [i for i in range(N)]
#     combi = list(combinations(nums, N // 2))
#
#     ans = 100000
#     for i in combi:
#         food2 = []
#         food1 = list(i)
#         for j in nums:
#             if j not in food1:
#                 food2.append(j)
#
#         sumf1 = sumf2 = 0
#         for k in range(N // 2 - 1):
#             for l in range(k + 1, N // 2):
#                 sumf1 += my_sum(k, l, arr, food1)
#                 sumf2 += my_sum(k, l, arr, food2)
#
#         t_ans = abs(sumf1 - sumf2)
#         if t_ans < ans:
#             ans = t_ans
#     print(f'#{tc}', ans)