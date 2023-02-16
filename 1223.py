import sys
sys.stdin = open('input.txt', 'r')

T = 10
def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '*':
        return v1 * v2

def step1(exp):
    icp = {'+': 1, '*': 2}
    isp = {'+': 1, '*': 2}

    ST = []
    result = []
    for c in exp:
        if c.isdigit():
            result.append(c)

        else:
            if ST and isp[ST[-1]] >= icp[c]:
                result.append(ST.pop())
                ST.append(c)
            else:
                ST.append(c)

    while ST:
        result.append(ST.pop())

    return result

def step2(exp):
    ST= []
    for c in exp:
        if c.isdigit():
            ST.append(int(c))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1, v2, c))
    return ST[-1]

for tc in range(1, T+1):
    N = int(input())
    s = input()
    a = step1(s)
    print(f'#{tc} {step2(a)}')
