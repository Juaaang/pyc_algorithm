import sys
sys.stdin = open('input.txt', 'r')

def hexTobin():


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ARR = [input() for _ in range(N)]

    binARR = []
    hexTobin()
    print(binARR)