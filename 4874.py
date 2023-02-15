import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
ST = []

def cal(v1,v2,op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v1 - v2
    if op == '*':
        return v1 * v2
    if op == '/':
        return v1 // v2

def step2(exp):
    ST = []
    for c in exp:
        if c == '.':
            break
        if c.isdigit():
            ST.append(int(c))
        else:
            if len(ST) > 1:
                v2 = ST.pop()
                v1 = ST.pop()
                ST.append(cal(v1, v2, c))
            else:
                ST.pop()
                break
    if len(ST) != 1:
        return 'error'
    else:
        return ST[-1]

for tc in range(1, T+1):
    s = list(input().split())
    print(f'#{tc}', step2(s))
