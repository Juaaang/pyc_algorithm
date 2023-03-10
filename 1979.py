'''

가로 세로 돌면서 연속되는 1의 length 가  K이면
출력
5<= N <= 15
2<= K <= N

가로 세로 나누지 않고 푸는 방법 생각해보기
경계 지점에 0추가
board = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
'''


import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         length = 0
#         for j in range(N):
#             if board[i][j] == 1:
#                 length += 1
#             else:
#                 if length == K:
#                     cnt += 1
#                 length = 0
#         if length == K:
#             cnt += 1
#
#     for k in range(N):
#         length = 0
#         for c in range(N):
#             if board[c][k] == 1:
#                 length += 1
#             else:
#                 if length == K:
#                     cnt += 1
#                 length = 0
#         if length == K:
#             cnt += 1
#
#     print(f'#{tc} {cnt}')

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans+= 1
                cnt = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(zip(*arr))
    ans = count(arr) + count(arr_t)
    print(f'#{tc} {ans}')

