import sys
sys.stdin = open('input.txt', 'r')

def cal(v1, v2, lis):
    if lis[0]:
        return v1 + v2
    if lis[1]:
        return v1 - v2
    if lis[2]:
        return v1 * v2
    if lis[3]:
        if (v1 < 0 and v2 > 0) or (v2 < 0 and v1 > 0):
            return -(abs(v1) // abs(v2))
        else:
            return abs(v1) // abs(v2)

def solve(k, curV, t_op_lis):
    global cnt
    t_op_lis = op_lis[:]
    while :
    solve(k+1, curV+cal(v1, v2, op_lis), t_op_lis)




N = int(input())
lst = list(map(int, input().split()))
op_lis = list(map(int, input().split()))
maxV = -10**9
minV = 10**9
cnt = 0
solve(0, lst[0], op_lis)
