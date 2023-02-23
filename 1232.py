import sys
sys.stdin = open('input.txt', 'r')

def cal(v1, v2, op):
    if op == '+':
        return int(v1) + int(v2)
    if op == '-':
        return int(v1) - int(v2)
    if op == '*':
        return int(v1) * int(v2)
    if op == '/':
        return round(int(v1) / int(v2))

def func(lis):
    ST = []
    for i in lis:
        if i.isdigit():
            ST.append(i)
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            res = cal(v1, v2, i)
            ST.append(res)
    return ST

def postOrder(root):
    if root:
        postOrder(left[root])
        postOrder(right[root])
        lis.append(heap[root])
    return

T = 10
for tc in range(1,T+1):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)
    heap = [0]*(N+1)
    for _ in range(N):
        info = list(input().split())
        if len(info) == 4:
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
        heap[int(info[0])] = info[1]
    lis = []
    postOrder(1)
    ans = func(lis)
    print(f'#{tc}', *ans)

