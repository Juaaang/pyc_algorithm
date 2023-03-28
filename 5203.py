import sys
sys.stdin = open('input.txt', 'r')

def run_solve(p1, p2):
    for i in range(len(lis)-2):
        if p1[i] != 0 and p1[i + 1] != 0 and p1[i + 2] != 0:
            return 1
        if p2[i] != 0 and p2[i + 1] != 0 and p2[i + 2] != 0:
            return 2

def solve():
    for idx in range(6):
        p1[lis[2 * idx]] += 1
        p2[lis[1 + 2 * idx]] += 1
        if idx >= 2:
            if max(p1) >= 3 or run_solve(p1, p2) == 1:
                return 1
            if max(p2) >= 3 or run_solve(p1, p2) == 2:
                return 2
    return 0

T = int(input())
for tc in range(1,T+1):
    lis = list(map(int, input().split()))
    p1 = [0 for _ in range(12)]
    p2 = [0 for _ in range(12)]
    print(f'#{tc}', solve())




