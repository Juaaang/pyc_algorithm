import sys
sys.stdin = open('input.txt', 'r')

T = 10

def plus(v1, v2):
    return v1 + v2

def step1(exp):
    ST = []
    result = []
    for c in exp:
        if c.isdigit():
            result.append(c)
        else:
            if ST:
                result.append(ST.pop())
                ST.append(c)
            else:
                ST.append(c)
    while ST:
        result.append(ST.pop())

    return result

def step2(exp):
    ST = []
    for c in exp:
        if c.isdigit():
            ST.append(int(c))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(plus(v1,v2))
    return ST[-1]


for tc in range(1, T+1):
    N = int(input())
    s = input()
    a = step1(s)
    print(f'#{tc}', step2(a))