'''
N = 버스 노선 개수
i번째 버스 노선은 번호가 A_i 이상 B_i 이하인 모든 정류장만을 다니는 버스노선
P개의 버스정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하기

N : 노선의 수
Ai ~ Bi 숫자를 C에 넣어줌
P : C의 length
C : 결과값을 넣기 위한 값

해결방안
N을 반복문을 돌려서 A,B에 대해 찾고

'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnts = [0]*5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnts[i] += 1
    P = int(input())
    res_lis = []

    for _ in range(P):
        c = int(input())
        res_lis.append(cnts[c])
    print(f'#{tc}', *res_lis)

# for tc in range(1, T+1):
#     N = int(input())
#     # N번 반복하면서 노선입력, 빈도수 표시
#     cnts = [0]*5001
#     for _ in range(N):
#         S, E = map(int, input().split())
#         for i in range(S, E+1):
#             cnts[i] += 1
#     P = int(input())
#     alst = []
#     for _ in range(P):
#         c = int(input())
#         alst.append(cnts[c])
#
#     print(f"#{tc}", *alst)

