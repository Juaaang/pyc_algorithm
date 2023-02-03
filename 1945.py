'''
입력
10
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

N이 2로 나눠지면 a에 카운트 .. (%) 활용


'''

# T = int(input())
# for tc in range(1, T+1):
#     a = b = c = d = e = 0
#     N = int(input())
#     while N > 1:
#         if N % 2 == 0:
#             a += 1
#             N /= 2
#         if N % 3 == 0:
#             b += 1
#             N /= 3
#         if N % 5 == 0:
#             c += 1
#             N /= 5
#         if N % 7 == 0:
#             d += 1
#             N /= 7
#         if N % 11 == 0:
#             e += 1
#             N /= 11
#     print(f'#{tc} {a} {b} {c} {d} {e}')

import sys

sys.stdin = open('input.txt', 'r')
divs = [2,3,5,7,11]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnts = [0]*len(divs)

    for i in range(len(divs)):
        while N%divs[i] == 0:
            cnts[i]+=1
            N=N//divs[i]

    print(f'#{tc}', *cnts)