'''
결국 카운트정렬로 푸는 문제인데
문제 해결 아이디어를 도출하는 과정이 어려웠음
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnts = [0]*200
    for _ in range(N):
        S, E = map(int, input().split())
        if S > E:
            S, E = E, S
        for i in range((S-1)//2, (E-1)//2 +1):
            cnts[i] += 1
    res = max(cnts)
    print(f'#{tc} {res}')