import sys
sys.stdin = open('input.txt', 'r')

def cal(v1,v2,op):
    global curS
    if op == ops[0]:
        return v1 + v2
    if op == ops[1]:
        return v1 - v2
    if op == ops[2]:
        return v1 * v2
    if op == ops[3]:
        if v1 < 0:
            return -(abs(v1) // v2)
        else:
            return v1 // v2

def solve(k, curS):
    global minV, maxV

    if k == N-1:
        maxV = max(curS, maxV)
        minV = min(curS, minV)
        return
    for i in range(4):
        if ops_cnt[i]:
            ops_cnt[i] -= 1
            solve(k + 1, cal(curS, nums[k + 1], ops[i]))
            ops_cnt[i] += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ops_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ops = ['+', '-', '*', '/']
    maxV = -10**8
    minV = 10**8
    solve(0, nums[0])
    print(f'#{tc} {maxV - minV}')

