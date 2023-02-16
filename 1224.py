import sys
sys.stdin = open('input.txt', 'r')

T = 10

icp = {'+' : 1, '*' : 2, '(': 3}
isp = {'+' : 1, '*' : 2, '(': 0}

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '*':
        return v1 * v2

def step1(exp):
    ST = []
    result = []
    for i in exp:
        if i.isdigit():
            result.append(i)
        elif i == ')':
            while ST and ST[-1] != '(':
                result.append(ST.pop())
            ST.pop()
        else:
            if ST and isp[ST[-1]] >= icp[i]:
                result.append(ST.pop())
                ST.append(i)
            else:
                ST.append(i)
    while ST:
        result.append(ST.pop())

    return result

def step2(exp):
    ST = []
    for i in exp:
        if i.isdigit():
            ST.append(int(i))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1,v2,i))
    return ST[-1]

for tc in range(1, T+1):
    N = int(input())
    s = input()
    a = step1(s)
    print(f'#{tc}', step2(a))