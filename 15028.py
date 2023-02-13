import sys
sys.stdin = open('input.txt', 'r')

def isPair(input_s):
    stack = []
    t = 0
    for c in input_s:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')'or c == '}':
            if len(stack) == 0:
                return 0
            t = stack.pop()
            if t != '(' and t != '{':
                return 0
            elif c == ')' and t == '{':
                return 0
            elif c == '}' and t == '(':
                return 0

    if len(stack) > 0:
        return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    input_s = input()
    print(f'#{tc} {isPair(input_s)}')
